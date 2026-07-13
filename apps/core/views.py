from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.db.models import Avg, Count, Q
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import AvaliacaoForm, FeedbackForm, LoginForm, RegistroForm
from .models import Avaliacao, Categoria, Estabelecimento, Evento, Feedback
import json

EVENTOS_CATEGORIA_SLUG = 'eventos'


def purge_eventos_expirados():
    """Remove eventos 24h após o horário de término."""
    from django.utils import timezone

    agora = timezone.now()
    for evento in Evento.objects.filter(ativo=True):
        fim = evento.get_datetime_fim()
        if agora > fim + timedelta(hours=24):
            if evento.banner:
                evento.banner.delete(save=False)
            evento.delete()


def _eventos_destaque_carrossel():
    qs = Evento.objects.filter(ativo=True, destaque=True).order_by(
        'data_inicio', 'hora_inicio'
    )[:25]
    return [e for e in qs if not e.esta_encerrado()][:5]


def home(request):
    """Página inicial com categorias e estabelecimentos (ou eventos na categoria Eventos)."""
    purge_eventos_expirados()

    categorias = Categoria.objects.filter(ativo=True)
    categoria_selecionada_slug = request.GET.get('categoria')
    categoria_selecionada = None
    modo_eventos = categoria_selecionada_slug == EVENTOS_CATEGORIA_SLUG

    estabelecimentos_destaque = Estabelecimento.objects.filter(
        ativo=True,
        destaque=True
    ).select_related('categoria').annotate(
        media_avaliacoes=Avg('avaliacoes__estrelas'),
        total_avaliacoes=Count('avaliacoes')
    ).order_by('-criado_em')[:5]

    eventos_destaque = _eventos_destaque_carrossel()

    # Combine highlights for homepage
    if modo_eventos:
        destaques = eventos_destaque[:4]
    else:
        destaques = sorted(
            list(estabelecimentos_destaque) + list(eventos_destaque),
            key=lambda x: x.criado_em,
            reverse=True
        )[:4]

    if modo_eventos:
        estabelecimentos = Estabelecimento.objects.none()
        try:
            categoria_selecionada = Categoria.objects.get(
                slug=EVENTOS_CATEGORIA_SLUG, ativo=True)
        except Categoria.DoesNotExist:
            pass
        eventos_lista = Evento.objects.filter(ativo=True).order_by(
            'data_inicio', 'hora_inicio')
        estabelecimentos_por_categoria = []
    else:
        eventos_lista = []
        base_qs = Estabelecimento.objects.filter(ativo=True).select_related('categoria')

        if categoria_selecionada_slug:
            base_qs = base_qs.filter(
                categoria__slug=categoria_selecionada_slug)
            try:
                categoria_selecionada = Categoria.objects.get(
                    slug=categoria_selecionada_slug, ativo=True)
            except Categoria.DoesNotExist:
                pass

        estabelecimentos = base_qs.annotate(
            media_avaliacoes=Avg('avaliacoes__estrelas'),
            total_avaliacoes=Count('avaliacoes')
        )

        # Fileiras no estilo "Netflix": agrupa estabelecimentos por categoria.
        estabelecimentos_por_categoria = []
        if not categoria_selecionada_slug:
            anotado = (
                Estabelecimento.objects.filter(ativo=True)
                .select_related('categoria')
                .annotate(
                    media_avaliacoes=Avg('avaliacoes__estrelas'),
                    total_avaliacoes=Count('avaliacoes'),
                )
                .order_by('-destaque', '-criado_em')
            )
            by_cat = {}
            for est in anotado:
                if not est.categoria_id:
                    continue
                by_cat.setdefault(est.categoria_id, []).append(est)
            for cat in categorias:
                items = by_cat.get(cat.id, [])
                if items:
                    estabelecimentos_por_categoria.append({
                        'categoria': cat,
                        'estabelecimentos': items[:18],
                    })
        else:
            # Quando o usuário filtra uma categoria, mantém a experiência coerente
            # exibindo apenas uma "fileira" dessa categoria.
            if categoria_selecionada and estabelecimentos.exists():
                estabelecimentos_por_categoria = [{
                    'categoria': categoria_selecionada,
                    'estabelecimentos': list(estabelecimentos[:24]),
                }]

    context = {
        'categorias': categorias,
        'estabelecimentos': estabelecimentos,
        'estabelecimentos_por_categoria': estabelecimentos_por_categoria,
        'estabelecimentos_destaque': estabelecimentos_destaque,
        'eventos_destaque': eventos_destaque,
        'destaques': destaques,
        'categoria_selecionada': categoria_selecionada,
        'categoria_selecionada_slug': categoria_selecionada_slug,
        'modo_eventos': modo_eventos,
        'eventos_lista': eventos_lista,
        'feedback_form': FeedbackForm(),
    }
    return render(request, 'core/home.html', context)


def estabelecimento_detalhe(request, id):
    """Detalhes de um estabelecimento"""
    estabelecimento = get_object_or_404(
        Estabelecimento.objects.select_related(
            'categoria').prefetch_related('fotos', 'avaliacoes__usuario'),
        id=id,
        ativo=True
    )

    # Verificar se está nos favoritos do usuário
    is_favorito = False
    if request.user.is_authenticated:
        is_favorito = estabelecimento.favoritos.filter(
            id=request.user.id).exists()

    # Calcular média de avaliações
    avaliacoes = estabelecimento.avaliacoes.all()
    media_avaliacoes = avaliacoes.aggregate(
        Avg('estrelas'))['estrelas__avg'] or 0

    # Formulário de avaliação
    avaliacao_form = None
    usuario_ja_avaliou = False
    if request.user.is_authenticated:
        avaliacao_usuario = avaliacoes.filter(usuario=request.user).first()
        if avaliacao_usuario:
            usuario_ja_avaliou = True
            avaliacao_form = AvaliacaoForm(instance=avaliacao_usuario)
        else:
            avaliacao_form = AvaliacaoForm()

    context = {
        'estabelecimento': estabelecimento,
        'is_favorito': is_favorito,
        'avaliacoes': avaliacoes,
        'media_avaliacoes': round(media_avaliacoes, 1),
        'avaliacao_form': avaliacao_form,
        'usuario_ja_avaliou': usuario_ja_avaliou,
    }
    return render(request, 'core/estabelecimento_detalhe.html', context)


def eventos(request):
    """Lista de eventos"""
    purge_eventos_expirados()

    tipo_selecionado = request.GET.get('tipo')

    eventos_list = Evento.objects.filter(ativo=True).order_by(
        'data_inicio', 'hora_inicio')

    if tipo_selecionado:
        eventos_list = eventos_list.filter(tipo=tipo_selecionado)

    context = {
        'eventos': eventos_list,
        'tipo_selecionado': tipo_selecionado,
        'tipos': Evento.TIPO_CHOICES,
    }
    return render(request, 'core/eventos.html', context)


def evento_detalhe(request, id):
    """Detalhes de um evento (indisponível após o término)."""
    purge_eventos_expirados()
    evento = get_object_or_404(Evento.objects.prefetch_related('fotos'), id=id, ativo=True)
    if evento.esta_encerrado():
        raise Http404('Evento encerrado.')

    context = {
        'evento': evento,
    }
    return render(request, 'core/evento_detalhe.html', context)


def mapa_interativo(request):
    """Mapa interativo com todos os estabelecimentos e eventos"""
    purge_eventos_expirados()
    categoria_filtro = request.GET.get('categoria')

    # Contar estabelecimentos sem coordenadas
    estabelecimentos_sem_coordenadas_qs = Estabelecimento.objects.filter(
        ativo=True,
        latitude__isnull=True
    ) | Estabelecimento.objects.filter(
        ativo=True,
        longitude__isnull=True
    )
    total_sem_coordenadas = estabelecimentos_sem_coordenadas_qs.count()

    # Contar eventos sem coordenadas
    eventos_sem_coordenadas_qs = Evento.objects.filter(
        ativo=True,
        latitude__isnull=True
    ) | Evento.objects.filter(
        ativo=True,
        longitude__isnull=True
    )
    total_sem_coordenadas += eventos_sem_coordenadas_qs.count()
    
    # Querysets principais baseados no filtro de categorias
    if categoria_filtro == EVENTOS_CATEGORIA_SLUG:
        estabelecimentos = Estabelecimento.objects.none()
        eventos = Evento.objects.filter(
            ativo=True,
            latitude__isnull=False,
            longitude__isnull=False
        )
    elif categoria_filtro:
        estabelecimentos = Estabelecimento.objects.filter(
            ativo=True,
            categoria__slug=categoria_filtro,
            latitude__isnull=False,
            longitude__isnull=False
        ).select_related('categoria').annotate(
            media_avaliacoes=Avg('avaliacoes__estrelas'),
            total_avaliacoes=Count('avaliacoes')
        )
        eventos = Evento.objects.none()
    else:
        estabelecimentos = Estabelecimento.objects.filter(
            ativo=True,
            latitude__isnull=False,
            longitude__isnull=False
        ).select_related('categoria').annotate(
            media_avaliacoes=Avg('avaliacoes__estrelas'),
            total_avaliacoes=Count('avaliacoes')
        )
        eventos = Evento.objects.filter(
            ativo=True,
            latitude__isnull=False,
            longitude__isnull=False
        )

    categorias = Categoria.objects.filter(ativo=True)

    # Converter para JSON para o mapa
    pontos_json = []
    
    # Adicionar estabelecimentos
    for est in estabelecimentos:
        pontos_json.append({
            'id': est.id,
            'tipo_ponto': 'estabelecimento',
            'nome': est.nome,
            'categoria': est.categoria.nome,
            'endereco': est.endereco,
            'latitude': float(est.latitude),
            'longitude': float(est.longitude),
            'imagem': est.imagem_principal.url if est.imagem_principal else '',
            'descricao': est.descricao[:200] + '...' if len(est.descricao) > 200 else est.descricao,
            'horario': est.horario_funcionamento,
            'media_avaliacoes': round(est.media_avaliacoes or 0, 1),
            'url': f"/estabelecimento/{est.id}/"
        })

    # Adicionar eventos
    for ev in eventos:
        pontos_json.append({
            'id': ev.id,
            'tipo_ponto': 'evento',
            'nome': ev.nome,
            'categoria': f"Evento: {ev.get_tipo_display()}",
            'endereco': ev.localizacao,
            'latitude': float(ev.latitude),
            'longitude': float(ev.longitude),
            'imagem': ev.banner.url if ev.banner else '',
            'descricao': ev.descricao[:200] + '...' if len(ev.descricao) > 200 else ev.descricao,
            'horario': f"Início: {ev.data_inicio.strftime('%d/%m/%Y')} às {ev.hora_inicio.strftime('%H:%M')}",
            'media_avaliacoes': 0,
            'url': f"/evento/{ev.id}/"
        })

    # Criar uma lista misturada para renderizar na barra lateral
    pontos = list(estabelecimentos) + list(eventos)

    context = {
        'pontos': pontos,
        'pontos_json': json.dumps(pontos_json),
        'categorias': categorias,
        'categoria_filtro': categoria_filtro,
        'total_sem_coordenadas': total_sem_coordenadas,
    }
    return render(request, 'core/mapa_interativo.html', context)


def _enviar_email_ativacao(request, user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)
    link = request.build_absolute_uri(
        reverse('ativar_conta', kwargs={'uidb64': uid, 'token': token})
    )
    assunto = 'Confirme seu cadastro — Minha Vitrine'
    corpo = (
        f'Olá, {user.first_name or user.username}.\n\n'
        f'Para ativar sua conta, acesse o link abaixo:\n{link}\n\n'
        'Se você não se cadastrou, ignore este e-mail.'
    )
    send_mail(
        assunto,
        corpo,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )


def ativar_conta(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save(update_fields=['is_active'])
        messages.success(
            request, 'Conta ativada com sucesso! Você já pode entrar.')
        return redirect('login')
    messages.error(
        request, 'Link de ativação inválido ou expirado. Cadastre-se novamente.')
    return redirect('home')


def registro_view(request):
    """Registro de novos usuários"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                f'Bem-vindo, {user.first_name or user.username}! Sua conta foi criada com sucesso.',
            )
            return redirect('home')
    else:
        form = RegistroForm()

    return render(request, 'core/registro.html', {'form': form})


def login_view(request):
    """Login de usuários"""
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if not user.is_active:
                    messages.error(
                        request,
                        'Esta conta ainda não foi ativada. Verifique seu e-mail e clique '
                        'no link de confirmação.',
                    )
                else:
                    login(request, user)
                    messages.success(
                        request,
                        f'Bem-vindo de volta, {user.first_name or user.username}!',
                    )
                    next_url = request.GET.get('next', 'home')
                    return redirect(next_url)
            else:
                messages.error(request, 'Login ou senha incorretos.')
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})


@login_required
def logout_view(request):
    """Logout de usuários"""
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('home')


@login_required
def enviar_feedback(request):
    """Recebe feedback do usuário autenticado."""
    if request.method != 'POST':
        return redirect('home')
    form = FeedbackForm(request.POST)
    if form.is_valid():
        fb = form.save(commit=False)
        fb.usuario = request.user
        fb.save()
        messages.success(request, 'Obrigado pelo seu feedback!')
    else:
        messages.error(
            request,
            'Não foi possível enviar o feedback. Verifique a mensagem e tente novamente.',
        )
    return redirect(request.META.get('HTTP_REFERER') or 'home')


@login_required
def ver_feedbacks(request):
    """Painel de feedbacks enviados pelos usuários (somente admin)."""
    if not request.user.is_superuser:
        messages.error(request, 'Acesso restrito a administradores.')
        return redirect('home')
    feedbacks = Feedback.objects.select_related('usuario').order_by('-criado_em')
    return render(request, 'core/admin_feedbacks.html', {'feedbacks': feedbacks})


@login_required
def favoritar_estabelecimento(request, id):
    """Adicionar/remover estabelecimento dos favoritos"""
    estabelecimento = get_object_or_404(Estabelecimento, id=id)

    if request.user in estabelecimento.favoritos.all():
        estabelecimento.favoritos.remove(request.user)
        is_favorito = False
        mensagem = 'Estabelecimento removido dos favoritos'
    else:
        estabelecimento.favoritos.add(request.user)
        is_favorito = True
        mensagem = 'Estabelecimento adicionado aos favoritos'

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'is_favorito': is_favorito,
            'total_favoritos': estabelecimento.total_favoritos(),
            'mensagem': mensagem
        })

    messages.success(request, mensagem)
    return redirect('estabelecimento_detalhe', id=id)


@login_required
def meus_favoritos(request):
    """Lista de estabelecimentos favoritos do usuário"""
    estabelecimentos = request.user.estabelecimentos_favoritos.filter(
        ativo=True
    ).select_related('categoria').annotate(
        media_avaliacoes=Avg('avaliacoes__estrelas'),
        total_avaliacoes=Count('avaliacoes')
    )

    context = {
        'estabelecimentos': estabelecimentos,
    }
    return render(request, 'core/favoritos.html', context)


@login_required
def avaliar_estabelecimento(request, id):
    """Avaliar ou editar avaliação de um estabelecimento"""
    estabelecimento = get_object_or_404(Estabelecimento, id=id)

    avaliacao_existente = Avaliacao.objects.filter(estabelecimento=estabelecimento, usuario=request.user).first()

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST, instance=avaliacao_existente)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            if avaliacao_existente:
                avaliacao.editada = True
            else:
                avaliacao.estabelecimento = estabelecimento
                avaliacao.usuario = request.user
            avaliacao.save()
            msg = 'Avaliação atualizada com sucesso!' if avaliacao_existente else 'Avaliação enviada com sucesso!'
            messages.success(request, msg)
            return redirect('estabelecimento_detalhe', id=id)

    return redirect('estabelecimento_detalhe', id=id)


@login_required
def votar_avaliacao(request, id):
    if request.method != 'POST':
        return JsonResponse({'success': False, 'error': 'Método não permitido.'})
    
    avaliacao = get_object_or_404(Avaliacao, id=id)
    if avaliacao.usuario == request.user:
        return JsonResponse({'success': False, 'error': 'Você não pode votar na própria avaliação.'})
        
    try:
        data = json.loads(request.body)
        voto = data.get('voto') # 'util' ou 'inutil'
    except:
        return JsonResponse({'success': False, 'error': 'Dados inválidos.'})
    
    if voto == 'util':
        if request.user in avaliacao.votos_uteis.all():
            avaliacao.votos_uteis.remove(request.user)
            ativo = False
        else:
            avaliacao.votos_uteis.add(request.user)
            avaliacao.votos_inuteis.remove(request.user)
            ativo = True
    elif voto == 'inutil':
        if request.user in avaliacao.votos_inuteis.all():
            avaliacao.votos_inuteis.remove(request.user)
            ativo = False
        else:
            avaliacao.votos_inuteis.add(request.user)
            avaliacao.votos_uteis.remove(request.user)
            ativo = True
    else:
        return JsonResponse({'success': False, 'error': 'Voto inválido.'})
        
    return JsonResponse({
        'success': True,
        'votos_uteis': avaliacao.votos_uteis.count(),
        'votos_inuteis': avaliacao.votos_inuteis.count(),
        'ativo': ativo,
        'tipo': voto
    })

@login_required
def remover_avaliacao(request, id):
    if request.method == 'POST' and request.user.is_superuser:
        avaliacao = get_object_or_404(Avaliacao, id=id)
        est_id = avaliacao.estabelecimento.id
        avaliacao.delete()
        messages.success(request, 'Avaliação removida com sucesso.')
        return redirect('estabelecimento_detalhe', id=est_id)
    return redirect('home')

def buscar_ajax(request):
    """Busca rápida via AJAX (Live Search)"""
    query = request.GET.get('q', '').strip()
    if len(query) < 2:
        return JsonResponse({'results': []})
        
    estabelecimentos = Estabelecimento.objects.filter(
        Q(nome__icontains=query) | Q(categoria__nome__icontains=query),
        ativo=True
    ).select_related('categoria')[:5]

    eventos = Evento.objects.filter(
        Q(nome__icontains=query) | Q(descricao__icontains=query),
        ativo=True
    )[:5]
    
    results = []
    for est in estabelecimentos:
        results.append({
            'id': est.id,
            'tipo': 'estabelecimento',
            'nome': est.nome,
            'categoria': est.categoria.nome,
            'url': f"/estabelecimento/{est.id}/",
            'imagem': est.imagem_principal.url if est.imagem_principal else None
        })

    for ev in eventos:
        results.append({
            'id': ev.id,
            'tipo': 'evento',
            'nome': ev.nome,
            'categoria': f"Evento: {ev.get_tipo_display()}",
            'url': f"/evento/{ev.id}/",
            'imagem': ev.banner.url if ev.banner else None
        })
        
    return JsonResponse({'results': results[:6]})

def buscar(request):
    """Busca de estabelecimentos e eventos"""
    query = request.GET.get('q', '')
    categoria = request.GET.get('categoria')

    estabelecimentos = Estabelecimento.objects.filter(ativo=True)
    eventos = Evento.objects.filter(ativo=True)

    if query:
        estabelecimentos = estabelecimentos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(endereco__icontains=query)
        )
        eventos = eventos.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(localizacao__icontains=query)
        )

    if categoria:
        if categoria == EVENTOS_CATEGORIA_SLUG:
            estabelecimentos = Estabelecimento.objects.none()
        else:
            estabelecimentos = estabelecimentos.filter(categoria__slug=categoria)
            eventos = Evento.objects.none()

    estabelecimentos = estabelecimentos.select_related('categoria').annotate(
        media_avaliacoes=Avg('avaliacoes__estrelas'),
        total_avaliacoes=Count('avaliacoes')
    )

    context = {
        'estabelecimentos': estabelecimentos,
        'eventos': eventos,
        'query': query,
        'categoria_selecionada': categoria,
    }
    return render(request, 'core/busca.html', context)
