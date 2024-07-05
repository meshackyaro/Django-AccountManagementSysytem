from django.apps import AppConfig


class NewAccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'new_account'

    def ready(self) -> None:
        import new_account.signals
