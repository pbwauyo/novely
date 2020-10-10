from django import forms
from . import models


class AudioFileForm(forms.ModelForm):

    class Meta:
        model = models.AudioFile
        fields = '__all__'