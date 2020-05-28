from django.db import models

# Create your models here.
class Contactsapp(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contacts(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    body = models.TextField()
    type = models.ForeignKey(Contactsapp, on_delete=models.PROTECT, related_name='post')
    date_published = models.DateTimeField(auto_now_add=True)

    def html_body(self):
        return self.body.replace('\n', '<br>')

    def __str__(self):
        return self.title + ' - ' + self.author

    