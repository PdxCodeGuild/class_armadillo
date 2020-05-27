from django.contrib import admin

from .models import BlogPost, BlogPostType

admin.site.register(BlogPost)
admin.site.register(BlogPostType)
