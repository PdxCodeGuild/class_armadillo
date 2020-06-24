
from django.core.management.base import BaseCommand

from blogapp.models import BlogPost, BlogPostType, BlogPostTag







class Command(BaseCommand):

    def handle(self, *args, **options):

        # types - many-to-one / foreignkeyfield ======================

        # get a blog post and look at its type
        blog_post = BlogPost.objects.get(id=1)
        print(blog_post.title)
        print(blog_post.type.name)
        print()

        # get a blog post type and look at all the blog posts associated with it
        blog_post_type = BlogPostType.objects.get(id=1)
        print(blog_post_type.name)
        # blog_post_type.blogpost_set.all() - without the related name
        print(blog_post_type.posts.all()) # with the related name
        print()

        # tags - many-to-many =======================================

        # get a blog post
        blog_post = BlogPost.objects.get(title='Burrito')
        # get all the tags associated with a blog post
        print(blog_post.tags.all())
        
        # create a blog post tag
        # tag = BlogPostTag(name='#delicious')
        # save it to the database - necessary before we create a relationship with a blog post
        # tag.save()

        # check if a record exists, .exists returns true if .filter has any results
        # if BlogPostTag.objects.filter(name='#delicious').exists():
        #     tag = BlogPostTag.objects.get(name='#delicious')
        # else:
        #     tag = BlogPostTag(name='#delicious')
        #     tag.save()

        # get_or_create will get the record if it exists or create it
        # it returns a tuple, the first value is the record
        # the second is a boolean that's true if it's created
        tag, created = BlogPostTag.objects.get_or_create(name='#delicious')


        # creating a relationship with a blog post
        blog_post.tags.add(tag)
        # get all the tags associated with a blog post (again)
        print(blog_post.tags.all())
        # removing a relationship with a blog post
        blog_post.tags.remove(tag)
        # get all the tags associated with a blog post (again)
        print(blog_post.tags.all())

        # clear all the tags
        blog_post.tags.clear()
        


        



        


