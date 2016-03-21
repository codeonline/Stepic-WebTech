# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


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
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='likes')

    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

    def __unicode__(self):
        return self.title


# Answer - ответ
# text - текст ответа
# added_at - дата добавления ответа
# question - вопрос, к которому относится ответ
# author - автор ответа
class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)