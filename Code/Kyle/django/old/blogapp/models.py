from django.db import models

class BlogPostType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    # id = models.IntegerField...
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey(BlogPostType, on_delete=models.PROTECT, related_name='posts')
    date_published = models.DateTimeField(auto_now_add=True)
    
    def html_body(self):
        return self.body.replace('\n', '<br/>')
    
    def __str__(self):
        return self.title + ' - ' + self.author
