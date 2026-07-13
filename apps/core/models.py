from datetime import datetime, time

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


class Categoria(models.Model):
    """Categorias dos estabelecimentos (Moda, Gastronomia, Farmácia, etc.)"""
    nome = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    icone = models.CharField(max_length=50, blank=True,
                             help_text="Nome do ícone (ex: 'restaurant', 'store')")
    ativo = models.BooleanField(default=True)
    ordem = models.IntegerField(default=0, help_text="Ordem de exibição")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem', 'nome']

    def __str__(self):
        return self.nome


class Estabelecimento(models.Model):
    """Estabelecimentos/Lojas cadastrados no sistema"""

    # Informações básicas
    nome = models.CharField(
        max_length=200, verbose_name="Nome do Estabelecimento")
    categoria = models.ForeignKey(
        Categoria, on_delete=models.PROTECT, related_name='estabelecimentos')
    descricao = models.TextField(verbose_name="Descrição")

    # Endereço
    endereco = models.CharField(max_length=300)
    numero = models.CharField(max_length=20, blank=True)
    complemento = models.CharField(max_length=100, blank=True)
    cep = models.CharField(max_length=10, blank=True, verbose_name="CEP")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    # Contato
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(
        max_length=20, blank=True, verbose_name="WhatsApp")
    website = models.URLField(blank=True, verbose_name="Website")
    instagram = models.CharField(
        max_length=100, blank=True, verbose_name="Instagram")
    facebook = models.CharField(
        max_length=100, blank=True, verbose_name="Facebook")

    # Dados administrativos
    cpf_validator = RegexValidator(
        regex=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$',
        message="CPF deve estar no formato: XXX.XXX.XXX-XX"
    )
    cpf = models.CharField(
        max_length=14,
        blank=True,
        validators=[cpf_validator],
        verbose_name="CPF"
    )
    
    cnpj_validator = RegexValidator(
        regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$',
        message="CNPJ deve estar no formato: XX.XXX.XXX/XXXX-XX"
    )
    cnpj = models.CharField(
        max_length=18,
        blank=True,
        validators=[cnpj_validator],
        verbose_name="CNPJ"
    )
    proprietario = models.CharField(
        max_length=200, blank=True, verbose_name="Proprietário")

    # Horário de funcionamento
    horario_funcionamento = models.TextField(
        blank=True, verbose_name="Horário de Funcionamento")

    # Imagem principal
    imagem_principal = models.ImageField(
        upload_to='estabelecimentos/', blank=True, null=True)

    # Controle
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(
        default=False, verbose_name="Estabelecimento em destaque")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='estabelecimentos_criados')

    # Favoritos
    favoritos = models.ManyToManyField(
        User, related_name='estabelecimentos_favoritos', blank=True)

    class Meta:
        verbose_name = 'Estabelecimento'
        verbose_name_plural = 'Estabelecimentos'
        ordering = ['-destaque', '-criado_em']

    def __str__(self):
        return self.nome

    def clean(self):
        super().clean()
        if not self.cpf and not self.cnpj:
            raise ValidationError("É obrigatório preencher o CPF ou o CNPJ do estabelecimento.")

    def total_favoritos(self):
        return self.favoritos.count()
    
    def get_google_maps_url(self):
        """Retorna URL para abrir o endereço no Google Maps"""
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        else:
            # Se não tiver coordenadas, usa o endereço completo
            endereco_completo = f"{self.endereco}"
            if self.numero:
                endereco_completo += f", {self.numero}"
            if self.complemento:
                endereco_completo += f", {self.complemento}"
            return f"https://www.google.com/maps/search/?api=1&query={endereco_completo.replace(' ', '+')}"
    
    def get_google_maps_embed_url(self):
        """Retorna URL para embed do Google Maps"""
        if self.latitude and self.longitude:
            return f"https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d1000!2d{self.longitude}!3d{self.latitude}!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!2zM!5e0!3m2!1spt-BR!2sbr!4v1"
        return None


class FotoEstabelecimento(models.Model):
    """Fotos adicionais dos estabelecimentos"""
    estabelecimento = models.ForeignKey(
        Estabelecimento, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='estabelecimentos/fotos/')
    legenda = models.CharField(max_length=200, blank=True)
    ordem = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto do Estabelecimento'
        verbose_name_plural = 'Fotos dos Estabelecimentos'
        ordering = ['ordem', '-criado_em']

    def __str__(self):
        return f"Foto de {self.estabelecimento.nome}"


class Avaliacao(models.Model):
    """Avaliações dos estabelecimentos"""
    estabelecimento = models.ForeignKey(
        Estabelecimento, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='avaliacoes')
    estrelas = models.IntegerField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comentario = models.TextField(blank=True)
    editada = models.BooleanField(default=False)
    data_edicao = models.DateTimeField(auto_now=True)
    votos_uteis = models.ManyToManyField(User, related_name='avaliacoes_uteis', blank=True)
    votos_inuteis = models.ManyToManyField(User, related_name='avaliacoes_inuteis', blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-criado_em']
        unique_together = ['estabelecimento', 'usuario']

    def __str__(self):
        return f"{self.usuario.username} - {self.estrelas} estrelas - {self.estabelecimento.nome}"


class Evento(models.Model):
    """Eventos na cidade"""

    TIPO_CHOICES = [
        ('gastronomia', 'Gastronomia'),
        ('moda', 'Moda'),
        ('cultura', 'Cultura'),
        ('esporte', 'Esporte'),
        ('educacao', 'Educação'),
        ('tecnologia', 'Tecnologia'),
        ('outro', 'Outro'),
    ]

    # Informações básicas
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES,
                            default='outro', verbose_name="Tipo de Evento")
    descricao = models.TextField(verbose_name="Descrição")

    # Localização
    localizacao = models.CharField(max_length=300, verbose_name="Localização")
    latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True)

    # Data e hora
    data_inicio = models.DateField(verbose_name="Data de Início")
    hora_inicio = models.TimeField(verbose_name="Hora de Início")
    data_fim = models.DateField(
        null=True, blank=True, verbose_name="Data de Término")
    hora_fim = models.TimeField(
        null=True, blank=True, verbose_name="Hora de Término")

    # Banner/Imagem
    banner = models.ImageField(upload_to='eventos/', blank=True, null=True)

    # Controle
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(
        default=False, verbose_name="Evento em destaque")
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    criado_por = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='eventos_criados')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['data_inicio', 'hora_inicio']

    def __str__(self):
        return f"{self.nome} - {self.data_inicio}"

    def get_datetime_inicio(self):
        dt = datetime.combine(self.data_inicio, self.hora_inicio)
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt

    def get_datetime_fim(self):
        d = self.data_fim or self.data_inicio
        t = self.hora_fim if self.hora_fim is not None else time(23, 59, 59)
        dt = datetime.combine(d, t)
        if timezone.is_naive(dt):
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
        return dt

    def esta_encerrado(self):
        return timezone.now() > self.get_datetime_fim()


class FotoEvento(models.Model):
    """Fotos adicionais dos eventos"""
    evento = models.ForeignKey(
        Evento, on_delete=models.CASCADE, related_name='fotos')
    imagem = models.ImageField(upload_to='eventos/fotos/')
    legenda = models.CharField(max_length=200, blank=True)
    ordem = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Foto do Evento'
        verbose_name_plural = 'Fotos dos Eventos'
        ordering = ['ordem', '-criado_em']

    def __str__(self):
        return f"Foto de {self.evento.nome}"


class Feedback(models.Model):
    """Mensagens de feedback enviadas pelos usuários"""
    usuario = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feedbacks_enviados')
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'
        ordering = ['-criado_em']

    def __str__(self):
        return f'Feedback de {self.usuario.username} em {self.criado_em}'


class Profile(models.Model):
    """Perfil estendido do usuário"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    telefone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, verbose_name="Biografia")
    is_dev = models.BooleanField(
        default=False, verbose_name="É desenvolvedor/admin")

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return f"Perfil de {self.user.username}"
