from django.shortcuts import render

def home(request):
    if not request.user.is_authenticated:
        return render(request, 'account/login.html', {})

    return render(request, 'core/home.html', {})
