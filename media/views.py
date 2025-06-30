from django.shortcuts import render

from django.db import models

# Create your views here.
from rest_framework import viewsets, permissions

from .models import MediaFile

from .serializers import MediaFileSerializer


class MediaFieldViewset(viewsets.ModelViewSet):
    queryset = MediaFile.objects.all()
    serializer_class = MediaFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return MediaFile.objects.filter(models.Q(owner=user) | models.Q(is_public=True))