from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    birthday = models.DateField()
    # the phone number will be stored as 10 digits with no other characters
    phone_number = models.CharField(max_length=50)
    is_cell = models.BooleanField()
    comments = models.TextField(blank=True)

    # used in the admin panel, so you don't just see "Contact object (1)"
    # used in the template if you do {{contact}} - not such a great idea
    # used in the view - print(contact), s = str(contact)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + str(self.age) + ')'
    
    # class Meta:
    #     ordering = ['last_name']

