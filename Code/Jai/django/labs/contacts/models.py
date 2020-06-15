from django.db import models
from django.utils import timezone
from django import forms
# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age= models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(max_length=200)
    is_cell = models.BooleanField()
    comments = models.TextField(default='')

    def __str__(self):
        return self.first_name + ' ' + self.last_name 




'''
`first_name` | `CharField` | `<input type="text"/>` |
| `last_name` | `CharField` | `<input type="text"/>` |
| `age` | `IntegerField` | `<input type="number"/>` |
| `birthday` | `DateField` | `<input type="date"/>` |
| `phone_number` | `CharField` | `<input type="text" pattern="?"/>`
| `is_cell` | `BooleanField` | `<input type="checkbox"/>` |
| `comments` | `TextField`| `<textarea></textarea>` |
'''