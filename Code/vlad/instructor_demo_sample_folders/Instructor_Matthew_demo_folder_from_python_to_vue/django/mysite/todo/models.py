from django.db import models
from django.contrib.auth.models import User


class Priority(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' ' + str(self.todo_items.count())

class TodoItem(models.Model):
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todo_items')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='todo_items')
    
    def completed(self):
        return self.completed_date != None

    def __str__(self):
        return self.user.username + ': ' + self.description + ' - ' + self.priority.name

