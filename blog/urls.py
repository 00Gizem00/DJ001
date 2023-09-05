from django.urls import path
from . import views
from .views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="homepage"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("category/<str:cats>/", views.CategoryListView, name="category"),

]