from django.db import models

from api.utils.transliterate_filename import filename_to_ascii


def upload_to(instance, filename):
    return f'files/{filename_to_ascii(filename)}'


class File(models.Model):
    file = models.FileField(
        'Файл',
        upload_to=upload_to, )
    uploaded_at = models.DateTimeField(
        'Дата загрузки',
        auto_now_add=True,
    )
    processed = models.BooleanField(
        'Статус обработки',
        default=False,
    )

    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
