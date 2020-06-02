from django.db import models
from django.utils import timezone

# Create your models here.

class TodoItem(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)

# class ToDoList(models.Model):
#     description = models.CharField(max_length=50)
#     created_date = models.DateTimeField
#     completed_date = models.DateTimeField
#     completed = models.BooleanField

#     def __str__(self):
#         return self.description

# class ToDoItem(models.Model):
#     todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
#     specs = models.TextField

#     def __str__(self):
#         return self.specs