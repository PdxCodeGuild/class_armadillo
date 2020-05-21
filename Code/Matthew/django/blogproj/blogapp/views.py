from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import BlogPost

def index(request):
    posts = BlogPost.objects.order_by('-created_date').filter(approved=True)
    data = {
        'posts': posts
    }
    print(data)
    return render(request, 'blogapp/index.html', data)


def detail(request, blog_post_id):
    post = get_object_or_404(BlogPost, pk=blog_post_id)
    if not post.approved:
        raise Http404
    return render(request, 'blogapp/detail.html', {'post': post})

