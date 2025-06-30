from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_directory_path(instance, filename):
    return f"user_{instance.owner.id}/{filename}"

class MediaFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='media_files')
    file = models.FileField(upload_to=user_directory_path)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.file.name