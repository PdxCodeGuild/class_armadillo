from django.db import models


# Create your models here.


class PokemonType(models.Model):
    # max_length=200 make alway a max length so the user does not input more that is require by adding extract characters
    name = models.CharField(max_length=200)

    # Used in the admin panel so you don't see "Contact Object1" instead you see the first name and last name
    def __str__(self):  # we add this to have a string representation on the admin panel because if we do not have it  will show and object like "Contact Object1" or "Contact Object2" or "Contact Object3"instead of the first and last name
        # we add this only to the first and last name because everything else will be tight to the person first and last name this is why we only do it for the first and last
        return f'{self.name}'
        # (+ str(self.age)) this is to show the age add this at the end of last name inside the f string

    # to arrange the Poke type in alphabetical order do the following:
    class Meta:
        ordering = ['name']


class Pokemon(models.Model):

    number = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    height = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    image_front = models.CharField(max_length=50)
    image_back = models.CharField(max_length=50)
    types = models.ManyToManyField(PokemonType, related_name='pokemon')

    def __str__(self):
        return f'{self.name}  {self.number}'

    # to arrange the Poke type in alphabetical order do the following:
    class Meta:
        ordering = ['name']


# class Article(models.Model):
#     headline = models.CharField(max_length=100)
#     # publications = models.ManyToManyField(Publication)

#     class Meta:
#         ordering = ['headline']

#     def __str__(self):
#         return self.headline

# # Contacts can be singular because it is only represent one instance
# class Contacts(models.Model):
#     # max_length=200 make alway a max length so the user does not input more that is require by adding extract characters
#     first_name = models.CharField(max_length=200)
#     last_name = models.CharField(max_length=200)
#     age = models.IntegerField()  # default= 0
#     # default= "01/01/1999" if the user does not enter a birthday it will it input 01/01/1999
#     birthday = models.DateField(default="YYYY-MM-DD")
#     phone_number = PhoneField(
#         blank=True, help_text='Contact phone number', max_length=10)
#     # default=True = mean take anything and return true
#     is_cell = models.BooleanField(default=True)
#     # blank=True, = it is not require to fill it out   null=True=  if nothing is here dont crash
#     comments = models.TextField(max_length=200, blank=True, null=True)

#     # Used in the admin panel so you don't see "Contact Object1" instead you see the first name and last name
#     def __str__(self):  # we add this to have a string representation on the admin panel because if we do not have it  will show and object like "Contact Object1" or "Contact Object2" or "Contact Object3"instead of the first and last name
#         # we add this only to the first and last name because everything else will be tight to the person first and last name this is why we only do it for the first and last
#         return f'{self.first_name}  {self.last_name}'
#         # (+ str(self.age)) this is to show the age add this at the end of last name inside the f string
#         # also we can use  def __str__(self):  for the ???

    # to add a method to figure out the people birthday so we do not have to be adding the age manually
    # def age(self):
    #     return timezone.now().year - self.birthday.year

    # to rearrange everything by lastname
    # class Meta:
       # ordering = ['last_name']

# Django Tutorial = https://docs.djangoproject.com/en/3.0/intro/tutorial01/
# Django Quick tutorial = https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/Django%20Quickstart.md
