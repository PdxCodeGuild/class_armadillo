from django.db import models
from django import forms
from django.utils import timezone
import datetime

class Todos(models.Model):
    publish_date = models.DateField(blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
