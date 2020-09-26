from django.shortcuts import render

def listen_view(request):
    return render(request, 'listen/listen.html', {})
