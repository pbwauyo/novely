from django.shortcuts import render
from . import forms
from django.core.files.storage import FileSystemStorage
from . import models

def publish(request):
    return render(request, 'publish/publish.html', {})

def publish_new(request):
    return render(request, 'publish/publish_new.html', {})

def accept_license(request):
    return render(request, 'publish/accept_license.html', {})

def publish_done(request):
    return render(request, 'publish/publish_done.html', {})

def new_audio(request):
    if request.method == 'POST':
        form = forms.AudioFileForm(request.POST, request.FILES)

        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            voice = form.cleaned_data['voice']
            description = form.cleaned_data['description']

            audio_cover = request.FILES['audio-cover']
            audio_file = request.FILES['audio-file']

            fs = FileSystemStorage()

            audio_filename = fs.save(audio_file.name, audio_file)
            audio_cover_filename = fs.save(audio_cover.name, audio_cover)

            audio_file_url = fs.url(audio_filename)
            audio_cover_url = fs.url(audio_cover_filename)

            audio_file_model = models.AudioFile()
            audio_file_model.title = title
            audio_file_model.author = author
            audio_file_model.voice = voice
            audio_file_model.description = description
            audio_file_model.audio_cover_url = audio_cover_url
            audio_file_model.audio_url = audio_file_url
            audio_file_model.save() #save audio file

            return render(request, 'publish/accept_license.html', {'audio_file' : audio_file_model})

    else:
        form = forms.AudioFileForm()

    return render(request, 'publish/new_audio.html', {'audio_form' : form})