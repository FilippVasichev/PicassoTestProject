from http import HTTPStatus

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status

from api.models import File


@pytest.mark.django_db(transaction=True)
class TestFileApi:
    file_urls = reverse('files-list')
    file_upload_urls = reverse('files-upload')

    def test_files_urls(self, client):
        """
        Проверка существования эндпоинта files/.
        """
        try:
            response = client.get(self.file_urls)
        except Exception as e:
            assert False, (
                f'Страница "{self.file_urls}"  не работает. Ошибка: "{e}"'
            )
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Страница `{self.file_urls}` не найдена,'
            f' проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == HTTPStatus.OK, (
            f'Ошибка {response.status_code} при открытии '
            f'`{self.file_urls}`. Проверьте ее view-функцию'
        )

    def test_files_objects_response(self, client, file_1, file_2):
        """
        Проверка работоспособности эндпоинта files/.
        """
        response_json = client.get(self.file_urls).json()
        assert isinstance(response_json, list), (
            f'Убедитесь что в ответ на GET-запрос'
            f' к "{self.file_urls}" файлы представлены списком'
        )
        assert len(response_json) == File.objects.count(), (
            f'Убедитесь что в ответ на GET-запрос к "{self.file_urls}"'
            f'приходит список со всеми файлами.'
        )

    def test_files_upload_urls(self, client):
        """
        Проверка существования эндпоинта files/upload/.
        """
        try:
            response = client.get(self.file_upload_urls)
        except Exception as e:
            assert False, (
                f'Страница "{self.file_upload_urls}"  не работает.'
                f' Ошибка: "{e}"'
            )
        assert response.status_code != HTTPStatus.NOT_FOUND, (
            f'Страница `{self.file_upload_urls}` не найдена,'
            f' проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED, (
            f'Ошибка {response.status_code} при открытии '
            f'`{self.file_upload_urls}`. Проверьте ее view-функцию'
        )

    @pytest.mark.parametrize(
        'file_name, content_type', [
            ('test_file.jpg', 'image/jpg'),
            ('test_file.txt', 'text/plain'),
        ]
    )
    def test_file_upload(self, client, file_name, content_type, mock_media):
        """
        Проверка работоспособности эндпоинта
        api/files/upload для разных типов файлов.
        """
        file_for_upload = SimpleUploadedFile(
            file_name,
            b'test file content',
            content_type=content_type,
        )
        response = client.post(
            self.file_upload_urls,
            {'file': file_for_upload},
        )
        assert response.status_code == status.HTTP_201_CREATED, (
            'Ошибка при загрузке файла'
        )
