from django.db import models

class AudioFile(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.CharField(max_length=200, verbose_name='Author')
    voice = models.CharField(max_length=200, verbose_name='Voice')
    audio_cover_url = models.CharField(max_length=300, verbose_name='Audio Cover Url', blank=True)
    description = models.CharField(max_length=1000, verbose_name='Description')
    audio_url = models.CharField(max_length=100, verbose_name='Audio Url', blank=True)
