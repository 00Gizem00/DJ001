from django.shortcuts import render, get_object_or_404
from .models import Category, News

def index(request):
    categories = Category.objects.all()
    return render(request, 'pages/index.html', {'categories': categories})

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    news_in_category = News.objects.filter(category=category).order_by('-created')
    return render(request, 'pages/category_detail.html', {'category': category, 'news_in_category': news_in_category})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    return render(request, 'pages/news_detail.html', {'news': news})