from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth import (
    authenticate, 
    login as auth_login, 
)

def get_data_from_post(request, fields):
    fields_dict = dict()
    for field in fields:
        input_value = request.POST.get(field)
        fields_dict[field] = input_value
    return fields_dict


def validate_and_login_redirect(request, username, password):
    valid_user = authenticate(
        request, 
        username=username, 
        password=password
    )
    if valid_user is not None:
        auth_login(request, valid_user)
        print('valid user')
        return redirect(reverse_lazy('articles:feed'))
    else:
        print('invalid user')
        return HttpResponse('Login failed for given information.')

