from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=99)
    phone_number = models.CharField(max_length=20)
    is_cell = models.BooleanField(max_length=20)	
    comments = models.TextField(max_length=99)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'










# # Create your models here.
# class CapitalCity(models.Model):
#     name = models.CharField(max_length=200)

#    

# class Country(models.Model):
#     name = models.CharField(max_length=200)
#     capital = models.OneToOneField(CapitalCity, on_delete=models.CASCADE)
#     population = models.IntegerFIelds()
#     gdp = models.FloatField()
#     hot_or_not = models.BooleanField(default=True)
#     founding_day = models.DateTimeField()
#     ending_day = models. DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return self.name



# class City(models.Model):
#     name = models.CharField(max_length=200)

#         def _str__(self):
#             return self.name

# class User(models.Model):
#     name = models.CHarField(max_length=200)
#     city = models.ForeignKey(CIty, on_delete=models.PROTECT)

#     def __str__(self)
#         return self.name

# class Author(models.Model)
#     return = models.CHarField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#         name = models.CharField((max_length=200)
#         authors = models.ManyTOMany Field(Author, related_name='books')from django.db import models

# # Create your models here.
# class CapitalCity(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name

# class Country(models.Model):
#     name = models.CharField(max_length=200)
#     capital = models.OneToOneField(CapitalCity, on_delete=models.CASCADE)
#     population = models.IntegerFIelds()
#     gdp = models.FloatField()
#     hot_or_not = models.BooleanField(default=True)
#     founding_day = models.DateTimeField()
#     ending_day = models. DateTimeField(null=True, blank=True)

#     def__str__(self):
#         reutrn self.name



# class City(models.Model):
#     name = models.CharField(max_length=200)

#         def _Str__(self):
#             return self.name

# class User(models.Model):
#     name = models.CHarField(max_length=200)
#     city = models.ForeignKey(CIty, on_delete=models.PROTECT)

#     def __str__(self)
#         return self.name

# class Author(models.Model)
#     return = models.CHarField(max_length=200)

#     def __str__(self):
#         return self.name

# class Book(models.Model):
#         name = models.CharField((max_length=200)
#         authors = models.ManyTOMany Field(Author, related_name='books')