from django.shortcuts import render

def publish(request):

    return render(request, 'publish/publish.html', {})

def publish_new(request):
    return render(request, 'publish/publish_new.html', {})