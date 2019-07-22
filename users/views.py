from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.forms import CustomUserCreationForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages from django.contrib improve UX
            messages.success(request, ('User logged in!'))
            return redirect('home')
        else:
            messages.success(request, ('Error please try again!'))
            return redirect('login')
    else:
        return render(request, 'login.html')


def sign_up(request):
    if request.method == 'POST':
        # CustomUserCreationForm necessary if CustomUser's being used
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # cleaned_data attribute necessary for is_valid() method
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You successfully signed up!'))
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'sign_up.html', {'form': form})


def logout_user(request):
    # Simple logout using django.contrib.auth module
    logout(request)
    messages.success(request, ('User logged out!'))
    return redirect('home')# Create your views here.
