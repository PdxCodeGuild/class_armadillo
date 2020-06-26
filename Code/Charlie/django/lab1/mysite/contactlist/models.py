from django.db import models
# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True,null=True)
    birthday = models.DateField(default= "MM/DD/YYYY")
    email = models.EmailField()
    phone_number = models.CharField(max_length=15,blank=True,null=True) 
    is_cell = models.BooleanField()   
    comments = models.TextField(max_length=20)



    def __str__(self):
        return self.last_name + ', ' + self.first_name 

   