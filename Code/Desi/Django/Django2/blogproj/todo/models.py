from django.db import models

from django.utils import timezone

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=20)
    description = models.IntegerField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    priority= models.IntegerField(default=0)