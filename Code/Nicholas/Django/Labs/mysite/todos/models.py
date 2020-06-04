from django.db import models
import datetime
from django.utils import timezone

class TodoItem(models.Model):
    task = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.task 
