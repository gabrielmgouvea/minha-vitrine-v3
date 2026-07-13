from django.urls import path
from . import views

urlpatterns = [
    # Página inicial
    path('', views.home, name='home'),

    # Autenticação
    path('registro/', views.registro_view, name='registro'),
    path(
        'ativar/<uidb64>/<token>/',
        views.ativar_conta,
        name='ativar_conta',
    ),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('feedback/', views.enviar_feedback, name='enviar_feedback'),
    path('painel/feedbacks/', views.ver_feedbacks, name='ver_feedbacks'),

    # Estabelecimentos
    path('estabelecimento/<int:id>/', views.estabelecimento_detalhe,
         name='estabelecimento_detalhe'),
    path('estabelecimento/<int:id>/favoritar/',
         views.favoritar_estabelecimento, name='favoritar_estabelecimento'),
    path('estabelecimento/<int:id>/avaliar/',
         views.avaliar_estabelecimento, name='avaliar_estabelecimento'),
    path('avaliacao/<int:id>/votar/', views.votar_avaliacao, name='votar_avaliacao'),
    path('avaliacao/<int:id>/remover/', views.remover_avaliacao, name='remover_avaliacao'),

    # Eventos
    path('eventos/', views.eventos, name='eventos'),
    path('evento/<int:id>/', views.evento_detalhe, name='evento_detalhe'),

    # Mapa
    path('mapa/', views.mapa_interativo, name='mapa_interativo'),

    # Favoritos
    path('favoritos/', views.meus_favoritos, name='meus_favoritos'),

    # Busca
    path('buscar/', views.buscar, name='buscar'),
    path('buscar-ajax/', views.buscar_ajax, name='buscar_ajax'),
]
