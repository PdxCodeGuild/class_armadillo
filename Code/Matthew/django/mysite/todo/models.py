from django.db import models

class TodoItem(models.Model):
    description = models.CharField(max_length=500)
    created_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField()

    def __str__(self):
        return self.description


