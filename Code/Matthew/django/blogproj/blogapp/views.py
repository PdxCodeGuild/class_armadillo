from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from .models import BlogPost, BlogPostType

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

def create_post_page(request):
    blog_post_types = BlogPostType.objects.order_by('name')
    return render(request, 'blogapp/new.html', {'types': blog_post_types})


def save_post(request):
    # print(request.POST)

    title = request.POST['blog_post_title']
    author = request.POST['blog_post_author']
    type_id = request.POST['blog_post_type_id']
    body = request.POST['blog_post_body']

    post = BlogPost(title=title,
                    author=author,
                    type_id=type_id,
                    body=body,
                    created_date=timezone.now(),
                    approved=True)
    post.save()
    return HttpResponseRedirect(reverse('blogapp:detail', args=(post.id,)))
