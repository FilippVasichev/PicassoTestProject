# Generated by Django 3.2.3 on 2023-10-11 12:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231011_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата загрузки'),
        ),
    ]
