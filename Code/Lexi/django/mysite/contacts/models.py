from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    phone_number = models.CharField(unique=True, blank=True, max_length=10)
    is_cell = models.BooleanField()
    comments = models.TextField()

    def __str__(self):
        # last_name will be unicode strings.
        return f' {self.last_name} {self.age}'


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)