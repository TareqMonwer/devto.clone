from django.urls import path
from articles.views import feed, publish_article


app_name = 'articles'

urlpatterns = [
    path('', feed, name='feed'),
    path('publish/', publish_article, name='publish_article'),
]
