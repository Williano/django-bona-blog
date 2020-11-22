from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    # Starts signals to create author profile.
    def ready(self):
        from . import signals
