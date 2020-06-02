from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    image_front = models.CharField(max_length=200)
    image_back = models.CharField(max_length=200)
    types = models.ManyToManyField(Type, related_name='type')

    def __str__(self):
        return self.name