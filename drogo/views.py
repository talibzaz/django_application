from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'drogo/article_list.html', {'articles': articles})


@login_required(login_url='/accounts/login')
def article_create(request):
    return render(request, 'drogo/article_create.html')


def article_detail(request, slug):
    article = Article.objects.get(url=slug)
    return render(request, 'drogo/article_detail.html', {'article': article})
