from django.apps import AppConfig


class SnowXtremConfig(AppConfig):
    name = 'SnowXtrem'

    def ready(self):
        from . import signals
