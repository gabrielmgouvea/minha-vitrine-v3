from .models import Categoria


def categorias_ativas(request):
    """Disponibiliza categorias ativas globalmente para o layout base."""
    return {
        'categorias': Categoria.objects.filter(ativo=True).order_by('nome')
    }
