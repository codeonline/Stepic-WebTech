# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Question - вопрос
# title - заголовок вопроса
# text - полный текст вопроса
# added_at - дата добавления вопроса
# rating - рейтинг вопроса (число)
# author - автор вопроса
# likes - список пользователей, поставивших "лайк"
class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.OneToOneField(User)
    likes = models.CharField(max_length=255)


# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateField()
    question = models.CharField(max_length=255)
    author = models.OneToOneField(User)





