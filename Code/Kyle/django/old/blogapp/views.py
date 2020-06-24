from django.shortcuts import render

from django.http import HttpResponse

from .models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.order_by('date_published')
    context = {
        'blog_posts': blog_posts
    }
    return render(request, 'blogapp/index.html', context)

