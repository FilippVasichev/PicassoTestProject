# Generated by Django 3.2.3 on 2023-10-22 10:36

from django.db import migrations, models

import api.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=api.models.upload_to,
                                          verbose_name='Файл')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True,
                                                     verbose_name='Дата загрузки')),
                ('processed', models.BooleanField(default=False,
                                                  verbose_name='Статус обработки')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
                'ordering': ('-uploaded_at',),
            },
        ),
    ]
