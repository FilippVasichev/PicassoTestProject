from django.contrib.admin import ModelAdmin, register, site
from django.contrib.auth.models import Group

from .models import File


@register(File)
class FileAdmin(ModelAdmin):
    list_display = (
        'file',
        'uploaded_at',
        'processed',
    )
    list_editable = (
        'processed',
    )
    empty_value_display = '-пусто-'


site.unregister(Group)