from django.core.management.base import BaseCommand
from apps.core.models import Categoria


class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write('Criando categorias...')

        categorias = [
            {'nome': 'Moda', 'slug': 'moda', 'icone': 'fa-shirt', 'ordem': 1},
            {'nome': 'Gastronomia', 'slug': 'gastronomia',
                'icone': 'fa-utensils', 'ordem': 2},
            {'nome': 'Farmácia', 'slug': 'farmacia',
                'icone': 'fa-pills', 'ordem': 3},
            {'nome': 'Mercado', 'slug': 'mercado',
                'icone': 'fa-shopping-cart', 'ordem': 4},
            {'nome': 'Lanchonete', 'slug': 'lanchonete',
                'icone': 'fa-hamburger', 'ordem': 5},
            {'nome': 'Eventos', 'slug': 'eventos',
                'icone': 'fa-calendar-alt', 'ordem': 6},
            {'nome': 'Outros', 'slug': 'outros',
                'icone': 'fa-ellipsis-h', 'ordem': 7},
        ]

        for cat_data in categorias:
            categoria, created = Categoria.objects.get_or_create(
                slug=cat_data['slug'],
                defaults=cat_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'[OK] Categoria "{categoria.nome}" criada'))
            else:
                self.stdout.write(self.style.WARNING(
                    f'[INFO] Categoria "{categoria.nome}" ja existe'))

        self.stdout.write(self.style.SUCCESS(
            '\n[OK] Dados iniciais carregados com sucesso!'))
