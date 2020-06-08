from django.contrib import admin
import datetime
from django.utils import timezone

# Register your models here.
class todo(models.Model):
    name = models.CharField(max_length=20)
    description = models.IntegerField(nax_length=200)
    created = models.DateTImeIntegerField(auto_now_add=True)
    completed = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(default=False)
    priority= models.IntegerField(default=0)
    
    

    # def __str__(self):
        return f'{self.name} {self.image_front} {self.image_back}'

