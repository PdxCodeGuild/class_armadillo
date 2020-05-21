from django.shortcuts import render
from django.http import HttpResponse

from .models import BlogPost


# Create your views here.
def index(request):
    posts = BlogPost.objects.filter(approve=True)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/index.html', context)

def create_post_page(request):
    return  render(request, 'blog/new.html')