from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date publsihed')
    def __str__(self):
        return self.question_text


class Choise(models.Model):
    question = models.ForeignKey(Question)
    choise_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return  self.choise_text