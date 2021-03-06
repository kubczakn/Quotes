from django.db import models


# make models here

class Haiku(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=500)
    type = models.CharField(max_length=50, default='default')


class Question(models.Model):
    question_text = models.CharField(max_length=100)


class Choice(models.Model):
    choice_text = models.CharField(max_length=200)
