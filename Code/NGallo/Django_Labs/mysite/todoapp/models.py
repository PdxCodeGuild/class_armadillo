from django.db import models
from django import forms
from django.utils import timezone
import datetime

class Todos(models.Model):
    publish_date = models.DateTimeField('date published')
    completed_date = models.DateTimeField('date completed') 
    task = models.CharField(max_length=200)
    completed = forms.BooleanField()

    def __str__(self):
        return self.task
