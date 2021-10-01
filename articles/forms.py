from django import forms
from articles.models import Article
from django_quill.forms import QuillFormField


class ArticleForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Article
        fields = ['title', 'tags', 'content']
