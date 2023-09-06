from django.shortcuts import render, get_object_or_404
from .models import Category, News

def index(request):
    # Fetch the "Music" category
    music_category = get_object_or_404(Category, slug='music')

    # Query the last 6 news items in the "Music" category
    music_news = News.objects.filter(category=music_category).order_by('-created')[:6]
    tech_news = News.objects.filter(category__slug='tech').order_by('-created')[:5]
    game_news = News.objects.filter(category__slug='game').order_by('-created')[:5]
    magazine_news = News.objects.filter(category__slug='magazine').order_by('-created')[:5]
    anime_news = News.objects.filter(category__slug='anime').order_by('-created')[:5]

    # Fetch all categories
    categories = Category.objects.all()

    # Create a list to store the latest news for each category
    latest_news_by_category = []

    # Query the latest news for each category
    for category in categories:
        latest_news = News.objects.filter(category=category).order_by('-created').first()
        if latest_news:
            latest_news_by_category.append(latest_news)

    return render(request, 'pages/index.html', {'latest_news_by_category': latest_news_by_category, 'categories': categories, 'music_news': music_news, 'tech_news': tech_news, 'game_news': game_news, 'magazine_news': magazine_news, 'anime_new': anime_news},)

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    news_in_category = News.objects.filter(category=category).order_by('-created')
    categories = Category.objects.all()  # Pass the categories to the context
    return render(request, 'pages/category_detail.html', {'category': category, 'news_in_category': news_in_category, 'categories': categories})

def news_detail(request, news_slug):
    news = get_object_or_404(News, slug=news_slug)
    categories = Category.objects.all()  # Pass the categories to the context
    return render(request, 'pages/news_detail.html', {'news': news, 'categories': categories})
