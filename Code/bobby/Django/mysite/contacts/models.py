from django.db import models


# Create your models here.
class Contactsapp(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(max_length=3)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=12)
    is_cell = models.BooleanField()
    comments = models.TextField()
    
    

    def html_body(self):
        return self.body.replace('\n', '<br>')

    def __str__(self):
        return self.name

    