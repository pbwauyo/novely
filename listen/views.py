from django.shortcuts import render
from publish.models import AudioFile

def listen_view(request):
    audios = AudioFile.objects.all()
    return render(request, 'listen/listen.html', {'audios' : audios})

def listen_audio_view(request, pk):
    audio_file = AudioFile.objects.get(pk=pk)
    return render(request, 'listen/listen_audio.html', {'audio' : audio_file})
