from django.contrib import admin
from .models import Contacts

# Register your models here.

#sample of the admin panel for the Polls lab
# from django.contrib import admin
# from .models import Question, Choice

# admin.site.register(Question) # this will add question to the admin panel 
# admin.site.register(Choice) # this will add Choice to the admin panel 

admin.site.register(Contacts)