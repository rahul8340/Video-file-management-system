

from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True)
    tags = models.CharField(max_length=255, null=True, blank=True)
    fps = models.FloatField(null=True, blank=True)
    codec_type = models.CharField(max_length=20, null=True, blank=True)
    bitrate = models.IntegerField(null=True)  # New field for bitrate
    resolution = models.CharField(max_length=255, null=True)  # New field for resolution
    audio_codec_type = models.CharField(max_length=255, null=True)  # New field for audio codec type
    audio_channels = models.IntegerField(null=True)  # New field for audio channels
    audio_sample_rate = models.IntegerField(null=True)  # New field for audio sample rate
    uploaded_at = models.DateTimeField(auto_now_add=True)

 
