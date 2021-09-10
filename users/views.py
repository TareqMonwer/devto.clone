from django.http import HttpResponse, request
from django.contrib.auth import logout
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

from users.utils import (
    get_data_from_post, 
    validate_and_login_redirect
)
from users.forms import UserProfileForm

User = get_user_model()


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
    user_info = get_object_or_404(User, username=username)
    context = {'user_info': user_info}
    return render(request, 'users/profile.html', context)


def update_profile(request, username):
    user = get_object_or_404(User, username=username)
    context = {}
    if request.method == 'POST':
        post_form = UserProfileForm(
            request.POST, 
            request.FILES,
            instance=user.profile
        )
        if post_form.is_valid():
            post_form.save()
            return redirect(reverse_lazy('users:profile', args=[username]))
    else:
        form = UserProfileForm(instance=user.profile)
        context['form'] = form
        context['user_info'] = user
        return render(request, 'users/update_profile.html', context)
