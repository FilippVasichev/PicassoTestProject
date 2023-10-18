from celery.utils.log import get_task_logger

from api.models import File
from picasso_test.celery import app

logger = get_task_logger(__name__)

@app.task
def change_processed_status(instance_pk: int) -> None:
    logger.info(f'Запущена задача для file pk = {instance_pk}.')
    file = File.objects.get(pk=instance_pk)
    file.processed = True
    file.save()
    logger.info(f'Задача для file pk = {instance_pk} выполнена.')