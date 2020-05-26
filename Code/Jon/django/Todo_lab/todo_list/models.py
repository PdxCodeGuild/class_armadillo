from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class TodoItem(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField()
