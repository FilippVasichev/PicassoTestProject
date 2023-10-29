from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import File
from .serializers import FileSerializer


class FileViewSet(ReadOnlyModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = None

    @action(methods=['post'], detail=False)
    def upload(self, request, pk=None):
        serializer = FileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
