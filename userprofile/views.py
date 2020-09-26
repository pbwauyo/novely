from django.shortcuts import render

def user_profile(request):
    user = request.user
    return render(request, 'userprofile/profile.html', {'user': user})

def subscriptions(request):
    return render(request, 'userprofile/subscriptions.html', {})

def subscription_hours(request):
    return render(request, 'userprofile/subscription_hours.html', {})

def subscription_days(request):
    return render(request, 'userprofile/subscription_days.html', {})

def subscription_days_done(request):
    return render(request, 'userprofile/sub_days_done.html', {})

def subscription_hours_done(request):
    return render(request, 'userprofile/sub_hours_done.html', {})
