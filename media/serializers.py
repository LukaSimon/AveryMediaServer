from rest_framework import serializers
from .models import MediaFile

class MediaFileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    field_url = serializers.SerializerMetaclass()

    class Meta:
        model = MediaFile
        fields = ['id', 'owner', 'file', 'file_url', 'title', 'description', 'uploaded_at', 'is_pulbic']
    
    def get_file_url(self, obj):
        return obj.file.url if obj.file else None
