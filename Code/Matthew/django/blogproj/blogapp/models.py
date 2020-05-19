from django.db import models

# models are python classes that parallel tables in the database
# migrations synchronize our models with the database
# python manage.py makemigrations - stage the changes
# python manage.py migrate - apply the changes
# https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/docs/05%20-%20Models.md#class-table-representation

class BlogPost(models.Model):
    # charfield - represents a string with a maximum length
    title = models.CharField(max_length=100)
    # textfield - represents a string with an unlimited length
    body = models.TextField()
    # booleanfield - represents a boolean
    approved = models.BooleanField()
    # integerfield - represents an integer
    rating = models.IntegerField()

    # returns a string representation of the model
    # used by the admin panel
    def __str__(self):
        return self.title + ' - ' + self.body[:4]+'...'









