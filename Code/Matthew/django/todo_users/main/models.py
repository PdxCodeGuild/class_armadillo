from django.db import models
from users.models import User

class Priority(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    text = models.CharField(max_length=200)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todo_items')
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='todo_items')

    def __str__(self):
        return self.user.username + ': ' + self.text

