import shutil
import tempfile

import pytest

from api.models import File


@pytest.fixture
def mock_media(settings):
    """
    Переопределяет папку media/ для тестов
    и удаляет временные файлы после тестов.
    """
    with tempfile.TemporaryDirectory() as temp_directory:
        settings.MEDIA_ROOT = temp_directory
        yield temp_directory
    shutil.rmtree(temp_directory, ignore_errors=True)


@pytest.fixture
def file_1():
    file = tempfile.NamedTemporaryFile(suffix=".txt", delete=False).name
    return File.objects.create(file=file)


@pytest.fixture
def file_2():
    file = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False).name
    return File.objects.create(file=file)
