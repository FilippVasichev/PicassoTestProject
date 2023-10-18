import tempfile

import pytest

from api.models import File
from file_uploader.celery import app


@pytest.fixture()
def mock_media(settings):
    with tempfile.TemporaryDirectory() as temp_directory:
        settings.MEDIA_ROOT = temp_directory
        yield temp_directory


@pytest.fixture
def file_1():
    file = tempfile.NamedTemporaryFile(suffix=".txt").name
    return File.objects.create(file=file)


@pytest.fixture
def file_2():
    file = tempfile.NamedTemporaryFile(suffix=".jpg").name
    return File.objects.create(file=file)
