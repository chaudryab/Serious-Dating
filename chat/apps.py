from django.apps import AppConfig
import os
from django.conf import settings


class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'
    path = os.path.join(settings.BASE_DIR, 'chat')

