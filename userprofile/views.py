from django.shortcuts import render

def user_profile(request):
    user = request.user
    return render(request, 'userprofile/profile.html', {'user': user})

def subscriptions(request):
    return render(request, 'userprofile/subscriptions.html', {})

def subscription_100(request):
    return render(request, 'userprofile/subscription_100.html', {})

def subscription_200(request):
    return render(request, 'userprofile/subscription_200.html', {})

def subscription_200_done(request):
    return render(request, 'userprofile/sub_200_done.html', {})

def subscription_100_done(request):
    return render(request, 'userprofile/sub_100_done.html', {})
