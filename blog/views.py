from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.views.generic import ListView, DetailView



page_defaults = {
    'title': 'Page',
    'body': 'This is a page.'
}


class HomeView(ListView):
    model = News
    template_name = 'pages/index.html'
    cats = Category.objects.all()
    queryset = News.objects.filter(published=True).order_by('-created')

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['cat_menu'] = cat_menu
        return context



# def homepage(request):
#     # content = {
#     #     'title': 'Home',
#     #     'body': '<h1>This is the homepage.</h1>'
#     # }

#     # context = {**page_defaults, **content}

#     return render(request, "pages/index.html", {'category': Category.objects.all()})

def about(request):
    # content = {
    #     'title': 'About',
    #     'body': '<h1>This is the About.</h1>'
    # }

    # context = {**page_defaults, **content}
    

    return render(request, "pages/index.html")

def contact(request):
    content = {
        'title': 'Contact',
        'body': '<h1>This is the contact.</h1>'
    }

    context = {**page_defaults, **content}

    return render(request, "pages/page.html", context)

def news_detail(request, slug, *args, **kwargs):
    news = get_object_or_404(News, slug=slug)
    context = {
        'news': news,
        'title': news.title,
        'body': news.body
    }
    return render(request, "pages/news_detail.html", context)

# def category_detail(request, category_slug):
#     category = get_object_or_404(Category, slug=category_slug)
#     # Kategoriye ait haberleri burada alabilirsiniz
#     # Örneğin: news = category.news.all()
#     return render(request, 'category_detail.html', {'category': category})

def CategoryListView(request, cats):
    category_posts = News.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'pages/category_detail.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})
 
