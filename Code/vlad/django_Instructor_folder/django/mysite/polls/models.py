from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        # long way
        # question = Question.objects.get(id=self.question_id)
        # short way - orm magic
        return self.question.question_text + ' ' + self.choice_text


# choice = Choice.objects.get(id=1)
# print(choice.question.question_text) # the question associated with this choice

# question = Question.objects.get(id=1)
# choices = question.choice_set.all() # all the choices associated with a question

# choices = question.choices.all()




