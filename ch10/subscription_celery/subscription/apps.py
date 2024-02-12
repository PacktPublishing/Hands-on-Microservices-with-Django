import os
from django.apps import AppConfig
from django.core.cache import cache


class SubscriptionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subscription'

    def ready(self) -> None:
        if os.environ.get('RUN_MAIN'):
            from .models import Magazine
            magazines = Magazine.objects.all()
            cache.set("magazines", magazines)
            print('Magazines added to Django cache')
