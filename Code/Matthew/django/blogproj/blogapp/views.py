from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone

from .models import BlogPost, BlogPostType

# a page for listing all the blog posts
def index(request):
    # posts = BlogPost.objects.all()
    # show the most recent blogpost first, only show approved posts
    posts = BlogPost.objects.order_by('-created_date').filter(approved=True)
    context = {
        'posts': posts
    }
    return render(request, 'blogapp/index.html', context)


# a page for viewing the details of a blog post
def detail(request, blog_post_id):
    post = get_object_or_404(BlogPost, pk=blog_post_id)
    if not post.approved:
        raise Http404
    return render(request, 'blogapp/detail.html', {'post': post})

# a page for creating a new blog post
def create_post_page(request):
    blog_post_types = BlogPostType.objects.order_by('name')
    return render(request, 'blogapp/new.html', {'types': blog_post_types})


def save_post(request):
    # print(request.POST)

    # request.POST has the data from our form
    title = request.POST['blog_post_title']
    author = request.POST['blog_post_author']
    type_id = request.POST['blog_post_type_id']
    body = request.POST['blog_post_body']

    # create an instance of our model
    post = BlogPost(title=title,
                    author=author,
                    type_id=type_id,
                    body=body,
                    created_date=timezone.now(),
                    approved=True)
    # save the new record to the database
    post.save()
    
    # redirect back to the detail page
    return HttpResponseRedirect(reverse('blogapp:detail', args=(post.id,)))
