from django.contrib import admin
from .models import (
    Categoria, Estabelecimento, FotoEstabelecimento, Avaliacao, Evento,
    FotoEvento, Profile, Feedback,
)


class FotoEstabelecimentoInline(admin.TabularInline):
    model = FotoEstabelecimento
    extra = 1
    fields = ['imagem', 'legenda', 'ordem']


class FotoEventoInline(admin.TabularInline):
    model = FotoEvento
    extra = 1
    fields = ['imagem', 'legenda', 'ordem']


class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 0
    readonly_fields = ['usuario', 'estrelas', 'comentario', 'criado_em']
    can_delete = True


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'ativo', 'ordem']
    list_filter = ['ativo']
    search_fields = ['nome']
    prepopulated_fields = {'slug': ('nome',)}
    list_editable = ['ativo', 'ordem']


@admin.register(Estabelecimento)
class EstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'proprietario',
                    'ativo', 'destaque', 'criado_em']
    list_filter = ['categoria', 'ativo', 'destaque', 'criado_em']
    search_fields = ['nome', 'descricao', 'proprietario', 'endereco']
    readonly_fields = ['criado_em', 'atualizado_em', 'criado_por']
    list_editable = ['ativo', 'destaque']
    inlines = [FotoEstabelecimentoInline, AvaliacaoInline]

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'categoria', 'descricao', 'imagem_principal')
        }),
        ('Endereço', {
            'fields': ('endereco', 'numero', 'complemento', 'cep', 'latitude', 'longitude')
        }),
        ('Contato', {
            'fields': ('email', 'telefone', 'whatsapp', 'website', 'instagram', 'facebook')
        }),
        ('Dados Administrativos', {
            'fields': ('cpf', 'cnpj', 'proprietario', 'horario_funcionamento')
        }),
        ('Controle', {
            'fields': ('ativo', 'destaque', 'criado_em', 'atualizado_em', 'criado_por')
        }),
    )

    class Media:
        js = ('js/admin_masks.js',)

    def save_model(self, request, obj, form, change):
        if not change:  # Se está criando um novo objeto
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)


@admin.register(FotoEstabelecimento)
class FotoEstabelecimentoAdmin(admin.ModelAdmin):
    list_display = ['estabelecimento', 'legenda', 'ordem', 'criado_em']
    list_filter = ['estabelecimento', 'criado_em']
    search_fields = ['estabelecimento__nome', 'legenda']
    list_editable = ['ordem']


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['estabelecimento', 'usuario', 'estrelas', 'criado_em']
    list_filter = ['estrelas', 'criado_em']
    search_fields = ['estabelecimento__nome',
                     'usuario__username', 'comentario']
    readonly_fields = ['criado_em']


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'data_inicio',
                    'hora_inicio', 'ativo', 'destaque', 'criado_em']
    list_filter = ['tipo', 'ativo', 'destaque', 'data_inicio']
    search_fields = ['nome', 'descricao', 'localizacao']
    readonly_fields = ['criado_em', 'atualizado_em', 'criado_por']
    list_editable = ['ativo', 'destaque']
    inlines = [FotoEventoInline]

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'descricao', 'banner')
        }),
        ('Localização', {
            'fields': ('localizacao', 'latitude', 'longitude')
        }),
        ('Data e Hora', {
            'fields': ('data_inicio', 'hora_inicio', 'data_fim', 'hora_fim')
        }),
        ('Controle', {
            'fields': ('ativo', 'destaque', 'criado_em', 'atualizado_em', 'criado_por')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:
            obj.criado_por = request.user
        super().save_model(request, obj, form, change)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'criado_em']
    list_filter = ['criado_em']
    search_fields = ['mensagem', 'usuario__username', 'usuario__email']
    readonly_fields = ['usuario', 'criado_em']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefone', 'is_dev']
    list_filter = ['is_dev']
    search_fields = ['user__username', 'user__email', 'telefone']
    list_editable = ['is_dev']


# Customização do painel admin
admin.site.site_header = "Minha Vitrine - Administração"
admin.site.site_title = "Minha Vitrine Admin"
admin.site.index_title = "Bem-vindo ao painel administrativo"
