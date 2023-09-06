from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True, editable=True, blank=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True, editable=True, blank=True)
    body = models.TextField()
    # bu foto kismini simdilik boyle birakiyorum. butun fotolar internetten alinacak. media klasoru ile ugrasmicam.
    photo_one = models.URLField(max_length=200, null=True, blank=True)
    photo_two = models.URLField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', null=True, blank=True)

    
    class Meta:
        db_table = 'news'
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors', null=True, blank=True)
    
    class Meta:
        db_table = 'authors'
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    
    
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.name