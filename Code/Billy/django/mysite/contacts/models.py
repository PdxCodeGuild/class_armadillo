from django.db import models
from django.utils import timezone

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # age = models.IntegerField()
    birthday = models.DateTimeField()
    phone_number = models.CharField(max_length=20)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        return self.last_name + ', ' + self.first_name 

    def format_phone(self):
        return '(' + self.phone_number[:3] + ') ' + self.phone_number[3:6] + '-' + self.phone_number[6:]

    def age(self):
        today = timezone.now()
        years = today.year - self.birthday.year
        if today.month < self.birthday.month or (today.month == self.birthday.month and today.day < self.birthday.day):
            years -= 1
        return years