# anpr/models.py

from django.db import models

class UploadedVideo(models.Model):
    video = models.FileField(upload_to='videos/')
    detected_text = models.TextField(default="No text detected")
    output_excel = models.FileField(upload_to='', blank=True, null=True)  # stores Excel file
