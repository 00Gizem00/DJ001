from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/<slug:slug>/", views.blog_detail, name="blog_detail"),
]