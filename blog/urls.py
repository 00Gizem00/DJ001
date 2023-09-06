from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/<slug:category_slug>/', views.category_detail, name='category_detail'),
    path('news/<slug:news_slug>/', views.news_detail, name='news_detail'),
]
