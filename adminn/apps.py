from django.apps import AppConfig
import os
from django.conf import settings

class AdminnConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'adminn'
    path = os.path.join(settings.BASE_DIR, 'adminn')

