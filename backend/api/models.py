from django.db import models

from api.utils.transliterate_filename import filename_to_ascii


def upload_to(instance, filename):
    """
    Возвращает директорию для сохранения файла.
    """
    return f'files/{filename}'


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

    def save(self, *args, **kwargs):
        """
        Изменяем имя файла на транслитерированное значение перед сохранением.
        """
        self.file.name = filename_to_ascii(self.file.name)
        super(File, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-uploaded_at',)
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.file.name
