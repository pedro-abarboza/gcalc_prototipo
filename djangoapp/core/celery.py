from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# define o ambiente padrão Django para o módulo celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usa as configurações de 'CELERY' no seu settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega automaticamente as tarefas (tasks) dos aplicativos registrados em seu projeto Django
app.autodiscover_tasks()