from django.db import models
from phone_field import PhoneField

# to handle the phone number did the following:
#  downloaded and installed the https://pypi.org/project/django-phone-field/
# to be able to use the from phone_field import PhoneField
# PyPIPyPI
# django-phone-field Lightweight model and form field for phone numbers in Django(13 kB)

# Create your models here.

# add inside the class the following
# def __str__(self):
# return self.name

# remember to run migration after creating models
# change one thing at a time and run migration to make sur
# it is not breaking Django step by step to ensure it is working
# we can go to the db sqlite to see it
# go to the admin panel to see if I see the panels
# register the models to the admin panel

# Register your models here.

# sample of the admin panel for the Polls lab
# from django.contrib import admin
# from .models import Question, Choice

# admin.site.register(Question) # this will add question to the admin panel
# admin.site.register(Choice) # this will add Choice to the admin panel

# once I have the model I can go to the admin panel to add the input for the contact list such as fullname, email, phone, full address,
# Also you can add the field in the python
# if you delete the city it will delete the user in the Mother child class mother relationship If add PROTECT it i will only
# db sqlite I can right click and browse the user and the other tables to see how the field looks like
# I can update the table vias the terminal but remember to run migration
# I can access the fiels in the terminal by using the following user.city.name this wil give us the city
# user.id will give us the id or the user.city_id which will give me value 1 or 2 user.city.id this will give me the name of the person
# city.user

# field name	Django model field	html element
# first_name	CharField	<input type="text"/>
# last_name	CharField	<input type="text"/>
# age	IntegerField	<input type="number"/>
# birthday	DateField	<input type="date"/>
# phone_number	CharField	<input type="text" pattern="?"/>
# is_cell	BooleanField	<input type="checkbox"/>
# comments	TextField	<textarea></textarea>

#     # capital = models.OneToOneField(CapitalCity, on_delete=models.CASCADE)
#     # population = models.IntegerField()
#     # gdp = models.FloatField()
#     # hot_or_not = models.BooleanField(default=True)
#     # founding_day = models.DateTimeField()
#     # ending_day = models.DateTimeField(null=True, blank=True)


# Contacts can be singular because it is only represent one instance
class Contacts(models.Model):
    # max_length=200 make alway a max length so the user does not input more that is require by adding extract characters
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()  # default= 0
    # default= "01/01/1999" if the user does not enter a birthday it will it input 01/01/1999
    birthday = models.DateField(default="YYYY-MM-DD")
    phone_number = PhoneField(
        blank=True, help_text='Contact phone number', max_length=10)
    # default=True = mean take anything and return true
    is_cell = models.BooleanField(default=True)
    # blank=True, = it is not require to fill it out   null=True=  if nothing is here dont crash
    comments = models.TextField(max_length=200, blank=True, null=True)

    # Used in the admin panel so you don't see "Contact Object1" instead you see the first name and last name
    def __str__(self):  # we add this to have a string representation on the admin panel because if we do not have it  will show and object like "Contact Object1" or "Contact Object2" or "Contact Object3"instead of the first and last name
        # we add this only to the first and last name because everything else will be tight to the person first and last name this is why we only do it for the first and last
        return f'{self.first_name}  {self.last_name}'
        # (+ str(self.age)) this is to show the age add this at the end of last name inside the f string
        # also we can use  def __str__(self):  for the ???

    # to add a method to figure out the people birthday so we do not have to be adding the age manually
    # def age(self):
    #     return timezone.now().year - self.birthday.year

    # to rearrange everything by lastname
    # class Meta:
       # ordering = ['last_name']

# Django Tutorial = https://docs.djangoproject.com/en/3.0/intro/tutorial01/
# Django Quick tutorial = https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/Django%20Quickstart.md
