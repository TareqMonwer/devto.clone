from django.http import HttpResponse
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from users.utils import (
    get_data_from_post, 
    validate_and_login_redirect
)


def registration(request):
    if request.method == 'POST':
        form_data = get_data_from_post(
            request, 
            ['username', 'email', 'password']
        )
        try:
            User.objects.create_user(
                form_data['username'], 
                form_data['email'], 
                form_data['password']
            )
            return validate_and_login_redirect(
                request,
                form_data['username'],
                form_data['password']
            )
        except Exception as e:
            return HttpResponse(e)
    return render(request, 'users/registration.html')


def login(request):
    if request.method == 'POST':
        form_data = get_data_from_post(
            request,
            ['username', 'password']
        )
        return validate_and_login_redirect(
            request,
            form_data['username'],
            form_data['password']
        )
    else:
        return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse_lazy('users:login'))


def user_profile(request, username):
    return render(request, 'users/profile.html')
