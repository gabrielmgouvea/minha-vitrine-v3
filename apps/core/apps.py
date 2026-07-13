from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
    label = 'core'
    verbose_name = 'Minha Vitrine'

    def ready(self):
        from apps.core import signals  # noqa: F401
