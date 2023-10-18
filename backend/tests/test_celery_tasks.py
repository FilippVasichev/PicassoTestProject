import pytest
from api.tasks import change_processed_status

@pytest.mark.celery(result_backend='rpc', broker='pyamqp://guest@localhost//')
@pytest.mark.django_db(transaction=True)
class TestCeleryTask:

    def test_celery_task_upload(self, celery_app, celery_worker):
        """
        Проверка работоспособности celery таски для
        асинхронного изменения статуса файла.
        """
        @celery_app.task
        def test_task(file_1):
            old_file_processed_status = file_1.processed
            task_result = change_processed_status.delay(file_1.pk)
            assert task_result.get() == True
            new_file_processed_status = file_1.processed
            assert old_file_processed_status != new_file_processed_status
