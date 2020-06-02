from django.contrib import admin

from .models import BlogPost, BlogPostType, BlogPostTag

# add our models to the admin panel localhost:8000/admin
admin.site.register(BlogPost)
admin.site.register(BlogPostType)
admin.site.register(BlogPostTag)

