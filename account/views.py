from django.shortcuts import render, redirect
from .forms import AccountChangeForm, AccountCreationForm, AccountAuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):

    if request.method == 'POST':
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect('home')

    else:
        form = AccountAuthenticationForm()

    return render(request, 'account/login.html', {'login_form' : form})

def signup_view(request):

    if request.POST:
        form = AccountCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect('home')

    else: 
        form = AccountCreationForm()

    return render(request, 'account/signup.html', {"signup_form" : form})

def logout_view(request):
    return render(request, 'account/logout.html', {})

def logout_user(request):
    logout
    return redirect('login')
