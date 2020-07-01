from django.db import models

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    date_created = models.DateTimeField()
    date_completed = models.DateTimeField(null=True, blank=True)


