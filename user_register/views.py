from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken!')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                login(request, new_user)
                messages.success(request, f'User {username} is  created successfully!')
                return redirect('index')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User is logged in successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out successfully!')
    return redirect('login')


@login_required
def profile(request):
    return render(request, 'profile.html')


def reset_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password_2 = request.POST['new_password_2']
        if new_password != new_password_2:
            messages.error(request, 'Passwords do not match!')
            return redirect('profile')
        else:
            current_user = request.user
            if check_password(old_password, current_user.password):
                current_user.password = make_password(new_password)
                current_user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('login')
            else:
                messages.error(request, 'Incorrect password!')
                return redirect('profile')



