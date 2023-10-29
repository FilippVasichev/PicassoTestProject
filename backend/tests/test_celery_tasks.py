import pytest

from api.models import File
from api.tasks import change_processed_status


@pytest.mark.django_db(transaction=True)
class TestCeleryTask:

    def test_celery_task_upload(self, file_1, celery_worker):
        """
        Проверка работоспособности celery таски для
        асинхронного изменения статуса файла.
        """
        old_file_processed_status = file_1.processed
        assert old_file_processed_status == False
        task_result = change_processed_status.delay(file_1.pk)
        task_result.get()
        new_file_processed_status = File.objects.get(pk=file_1.pk).processed
        assert new_file_processed_status == True
