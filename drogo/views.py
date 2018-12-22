from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'drogo/article_list.html', {'articles': articles})


@login_required(login_url='/accounts/login')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save to db
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'drogo/article_create.html', {'form': form})


def article_detail(request, slug):
    article = Article.objects.get(url=slug)
    return render(request, 'drogo/article_detail.html', {'article': article})
