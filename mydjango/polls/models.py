from django.db import models

class Question(models.Model):
    question_txt = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    def __str__(self):
        return self.question_txt

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_txt