from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from articles.forms import ArticleForm
from articles.models import Article


def feed(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def publish_article(request):
    context = {}
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect(reverse_lazy('articles:feed'))
        else:
            return HttpResponse("<h1>Publishing Article Failed</h1>")
    else:
        context['form'] = ArticleForm
    return render(request, 'articles/publish.html', context)
