from django.shortcuts import render, get_object_or_404
from .models import Post



page_defaults = {
    'title': 'Page',
    'body': 'This is a page.'
}


def homepage(request):
    content = {
        'title': 'Home',
        'body': '<h1>This is the homepage.</h1>'
    }

    context = {**page_defaults, **content}

    return render(request, "pages/page.html", context)

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

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})