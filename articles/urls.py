from django.urls import path
from articles.views import feed


app_name = 'articles'

urlpatterns = [
    path('', feed, name='feed'),
]