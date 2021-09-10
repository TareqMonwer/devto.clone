from django import forms
from django.forms import fields
from articles.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']
