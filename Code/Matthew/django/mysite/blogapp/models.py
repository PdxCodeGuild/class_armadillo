from django.db import models



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey('BlogPostType', on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField('BlogPostTag', related_name='posts')
    created_date = models.DateTimeField()
    approved = models.BooleanField()

    def __str__(self):
        return self.title



class BlogPostTag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class BlogPostType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


