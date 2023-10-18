import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'picasso_test.settings')
app = Celery("picasso_test")
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
