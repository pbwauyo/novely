from django.shortcuts import render, redirect
from . import forms
from . import models
import cloudinary

def publish(request):
    audios = models.AudioFile.objects.all().filter(pk=request.user.id)
    return render(request, 'publish/publish.html', {'audios' : audios})

def publish_new(request, pk):
    audio_file = models.AudioFile.objects.get(pk=pk)
    return render(request, 'publish/publish_new.html', {'audio_file' : audio_file})

def accept_license(request, pk):
    return render(request, 'publish/accept_license.html', {'audio_file_id' : pk})

def publish_done(request, pk):
    audio_file = models.AudioFile.objects.get(pk=pk)
    return render(request, 'publish/publish_done.html', {'audio_file' : audio_file})

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

            audio_cover_res= cloudinary.uploader.upload(audio_cover)
            audio_file_res = cloudinary.uploader.upload(audio_file, resource_type = "video")

            audio_file_model = models.AudioFile()
            audio_file_model.title = title
            audio_file_model.author = author
            audio_file_model.voice = voice
            audio_file_model.description = description
            audio_file_model.audio_cover_url = audio_cover_res['secure_url']
            audio_file_model.audio_url = audio_file_res['secure_url']
            audio_file_model.save() #save audio file

            return redirect('accept-license', pk=audio_file_model.pk)

    else:
        form = forms.AudioFileForm()

    return render(request, 'publish/new_audio.html', {'audio_form' : form})