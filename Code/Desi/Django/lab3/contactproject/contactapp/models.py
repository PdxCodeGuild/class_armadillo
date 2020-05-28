from django.db import models

# Create your models here.
from django.db import models


class Contact(mpdels.Model):
    first_name = models.Charfield(max_length=50)
    last_name = models.Charfield(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    age	 = models.TextField()
    birthday = models.TextField()
    phone_number = models.TextField()
    is_cell	= models.TextField()
    comments = models.TextField()	

    def __str__(self):
        return f'{self.first_name} {self.last_name}'