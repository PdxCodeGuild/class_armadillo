from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    # the phone number will be stored as 10 digits with no other characters
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    is_cell = models.BooleanField()
    comments = models.TextField(blank=True)

    # used in the admin panel, so you don't just see "Contact object (1)"
    # used in the template if you do {{contact}} - not such a great idea
    # used in the view - print(contact), s = str(contact)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' (' + str(self.age()) + ')'

    def age(self):
        today = timezone.now()
        years = today.year - self.birthday.year
        if today.month < self.birthday.month or (today.month == self.birthday.month and today.day < self.birthday.day):
            years -= 1
        return years
    
    def formatted_phone_number(self):
        return '(' + self.phone_number[:3] + ') ' + self.phone_number[3:6] + '-' + self.phone_number[6:]
    
    # used to set a default ordering which will apply everywhere
    # class Meta:
    #     ordering = ['last_name']

