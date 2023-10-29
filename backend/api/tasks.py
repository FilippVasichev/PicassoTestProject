from celery import shared_task
from celery.utils.log import get_task_logger

from api.models import File

logger = get_task_logger(__name__)


@shared_task
def change_processed_status(instance_pk: int) -> None:
    """
    Обрабатывает статус файла, изменяет статус файла на - True.
    """
    logger.info(f'Запущена задача для file pk = {instance_pk}.')
    file = File.objects.get(pk=instance_pk)
    file.processed = True
    file.save()
    logger.info(f'Задача для file pk = {instance_pk} выполнена.')
