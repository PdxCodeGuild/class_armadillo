from django.contrib import admin

from .models import Country, CapitalCity, User, City, Author, Book

admin.site.register(Country)
admin.site.register(CapitalCity)
admin.site.register(User)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)
