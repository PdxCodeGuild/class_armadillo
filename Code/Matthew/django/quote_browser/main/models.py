from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=200)
    favqs_id = models.IntegerField()
    tags = models.ManyToManyField(Tag, related_name='quotes')

    def __str__(self):
        return self.text[:100] + '... - ' + self.author
