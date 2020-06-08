from django.db import models

class ShortenedURL(models.Model):
    code = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    counter = models.IntegerField()

    def __str__(self):
        return self.code + self.url + str(self.counter)

