from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import BlogPost

# view - python function that receives the http request and returns the http response
# the view does the heavy lifting
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/03%20-%20Views.md
def index(request):


    # http method - get, put, post, or delete
    print(request.method)

    # path - e.g. /blogapp/
    print(request.path)

    # query parameters
    # e.g. localhost:8000/blogapp/?a=1&b=2&c=3 becomes {'a':'1', 'b':'2', 'c':'3'}
    # e.g. https://www.google.com/search?q=armadillo
    print(request.GET)

    # form data - the name attributes of input elements are the keys, the values are whatever the user entered
    print(request.POST)

    # text response
    # return HttpResponse('hello world!')

    # get all the rows out of the BlogPost table
    # using the ORM - object relational mapping
    # we write statements in python, the ORM translates those into queries on the database
    blog_posts = BlogPost.objects.all()

    # we can iterate over the results using for-loop
    for blog_post in blog_posts:
        print(blog_post)

    # data context - dictionary containing data we'll use to render the template
    context = {
        'title': 'My Blog',
        'message': '',
        'fruits': ['apples', 'bananas', 'pears'],
        'blog_posts': blog_posts
    }
    # render the template
    # parameter 1 - request that we're given as a parameter to the view
    # parameter 2 - app name / template name
    # parameter 3 - data context
    return render(request, 'blogapp/index.html', context)


# make another view JUST to receive the form submission and redirect back to the first view
def save_blog_post(request):
    print(request.POST) # dictionary that contains the form data
    
    # get the data out of the dictionary of form data
    blog_post_title = request.POST['blog_post_title']
    blog_post_body = request.POST['blog_post_body']
    blog_post_rating = request.POST['blog_post_rating']
    print(blog_post_title, blog_post_body, blog_post_rating)

    # create an instance of our model, pass values as kwargs
    blog_post = BlogPost(title=blog_post_title,
                            body=blog_post_body,
                            rating=blog_post_rating,
                            approved=True)
    # save the instance of our model to the database
    blog_post.save()

    return HttpResponseRedirect('/blogapp/')

