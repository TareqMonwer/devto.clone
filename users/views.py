from django.shortcuts import render


def registration(request):
    return render(request, 'users/registration.html')


def login(request):
    return render(request, 'users/login.html')