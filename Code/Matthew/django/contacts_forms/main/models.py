from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField()
    birthday = models.DateField()
    over_21 = models.BooleanField()
    location = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='contacts')

    def __str__(self):
        return self.name

