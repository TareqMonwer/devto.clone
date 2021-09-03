from django.urls import path
from users.views import (
    registration, login, logout_view,
    user_profile,
)

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/<str:username>/', user_profile, name='profile'),
]