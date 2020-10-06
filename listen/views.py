from django.shortcuts import render

def listen_view(request):
    return render(request, 'listen/listen.html', {'range' : range(10)})

def listen_audio_view(request):
    return render(request, 'listen/listen_audio.html', {})
