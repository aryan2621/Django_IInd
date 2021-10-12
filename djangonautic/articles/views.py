from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(req):
  articles = Article.objects.all().order_by('date')
  return render(req, 'articles/article_list.html', {
    'articles': articles
  })

def article_details(req, slug):
  article = Article.objects.get(slug=slug)
  return render(req, 'articles/article_detail.html', {
    'article': article,
  })

@login_required(login_url='accounts:login')
def article_create(req):
  if req.method == 'POST':
    form = forms.CreateArticle(req.POST, req.FILES)
    
    if form.is_valid():
      # save article to db
      instance = form.save(commit=False)
      instance.author = req.user
      instance.save()
      return redirect('articles:list')
  else:
    form = forms.CreateArticle()
  return render(req, 'articles/article_create.html', {'form': form})