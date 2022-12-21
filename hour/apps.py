from django.apps import AppConfig


class HourConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hour'
    
    def ready(self):
        from jobs import updater
        updater.start()