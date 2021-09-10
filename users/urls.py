from django.urls import path
from users.views import (
    registration, login, logout_view,
    user_profile,
    update_profile,
)

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('users/<str:username>/', user_profile, name='profile'),
    path('users/<str:username>/update/', update_profile, name='update_profile'),
]
