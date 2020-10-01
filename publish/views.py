from django.shortcuts import render

def publish(request):
    return render(request, 'publish/publish.html', {})

def publish_new(request):
    return render(request, 'publish/publish_new.html', {})

def accept_license(request):
    return render(request, 'publish/accept_license.html', {})

def publish_done(request):
    return render(request, 'publish/publish_done.html', {})

def new_audio(request):
    return render(request, 'publish/new_audio.html', {})