from django.db import models
# equivalent to:
# from django.db.models import Model

# this question class inherits everything this model does - class is Uppercase
class Question(models.Model): # CharField is also a class name
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)