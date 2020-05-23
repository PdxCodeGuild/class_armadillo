from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approve = models.BooleanField()

    def __str__(self):
        return self.title