from django.http import HttpResponse
from django.contrib.auth import (
    authenticate, 
    login as auth_login, 
    logout
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.models import User


def registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            User.objects.create_user(
                username, email, password
            )
            valid_user = authenticate(
                request, 
                username=username, 
                password=password
            )
            if valid_user is not None:
                auth_login(request, valid_user)
                return redirect(reverse_lazy('articles:feed'))
            else:
                return HttpResponse('Login failed for given information.')
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'users/registration.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        valid_user = authenticate(
            request, 
            username=username, 
            password=password
        )
        if valid_user is not None:
            auth_login(request, valid_user)
            return redirect(reverse_lazy('articles:feed'))
        else:
            return HttpResponse('Login failed for given information.')
    else:
        return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))