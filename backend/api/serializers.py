from rest_framework import serializers
from .models import File
from api.tasks import change_processed_status

class FileSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения всех Файлов.
    """
    class Meta:
        model = File
        fields = (
            'file',
            'uploaded_at',
            'processed',
        )

    def create(self, validated_data):
        instance = File.objects.create(**validated_data)
        change_processed_status.delay(instance_pk=instance.pk)
        return instance