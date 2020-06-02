from django.db import models


class Contact(mpdels.Model):
    first_name = models.Charfield(max_length=50)
    last_name = models.Charfield(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
        