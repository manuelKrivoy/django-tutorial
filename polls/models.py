
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text ## returns the question text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # returns True if the question was published within the last day


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) ## class Choice has a foreign key to class Question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text ## returns the choice text
