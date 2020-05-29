from django.db import models


class CapitalCity(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=200)
    capital = models.OneToOneField(CapitalCity, on_delete=models.CASCADE)
    population = models.IntegerField()
    gdp = models.FloatField()
    hot_or_not = models.BooleanField(default=True)
    founding_day = models.DateTimeField()
    ending_day = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name='users')

    def __str__(self):
        return self.name



class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    authors = models.ManyToManyField(Author, related_name='books')

    def __str__(self):
        return self.name


