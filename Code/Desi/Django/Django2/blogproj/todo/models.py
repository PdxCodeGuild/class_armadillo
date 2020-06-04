from django.db import models
from datetime
from django.utils import timezone

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=20)
    description = models.IntegerField(nax_length=200)
    created = models.DateTImeIntegerField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    priority= models.IntegerField(default=0)