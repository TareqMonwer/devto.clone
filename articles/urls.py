from django.urls import path
from articles.views import feed, publish_article, article_detail


app_name = 'articles'

urlpatterns = [
    path('', feed, name='feed'),
    path('publish/', publish_article, name='publish_article'),
    path('details/<int:pk>/', article_detail, name='detail'),
]
