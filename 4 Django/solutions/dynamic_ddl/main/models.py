from django.db import models

class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.PROTECT, related_name='cities')

    def __str__(self):
        return self.name

