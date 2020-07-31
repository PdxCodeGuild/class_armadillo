from django.db import models



class Priority(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TodoItem(models.Model):
    text = models.CharField(max_length=500)
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT, related_name='todo_items')
    created_date = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.priority.name + ' - ' + self.text







