# coding=utf-8

# Обработка форм

# 1) Разверните репозиторий со своим проектом в директориию /home/box

# 2) В файле qa/forms.py  создайте следующие формы для добавления вопроса и ответа.

# AskForm - форма добавления вопроса
# title - поле заголовка
# text - поле текста вопроса

# AnswerForm - форма добавления ответа
# text - поле текста ответа
# question - поле для связи с вопросом

# Имена классов форм и полей важны! Конструкторы форм должны получать стандартные для Django-форм аргументы, 
# т.е. должна быть возможность создать объект формы как AskForm() или AnswerForm(). 
# На данном этапе формы могут не учитывать авторизацию пользователей, т.е. создавать вопросы и ответы с произвольным либо пустым автором. 
# В формах реализуйте необходимые методы для валидации и сохранения данных (clean и save)

# 3) Создайте view и шаблоны для отображения и сохранения форм

# URL = /ask/

# При GET запросе - отображается форма AskForm, при POST запросе форма должна создавать новый вопрос и перенаправлять на страницу вопроса - /question/123/

# URL = /question/123/

# При GET запросе должна отображаться страница ответа и на ней AnswerForm

# URL = /answer/

# При POST запросе форма AnswerForm добавляет новый ответ и перенаправляет на страницу вопроса /question/123/

# Для поддержки CSRF защиты - выведите в шаблонах форм {% csrf_token %}.
from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
	title = forms.CharField(label="Question title:", required=True)
	text = forms.CharField(label="Question text:", widget=forms.Textarea, required=True)	

	def clean_title(self):
	 	title = self.cleaned_data['title']
	# 	if len(title) == 0:
	# 		raise forms.ValidationError(
	# 			u'Empty title', code=1)
	 	return title

	def clean_text(self):
	 	text = self.cleaned_data['text']
	# 	if len(text) == 0:
	# 		raise forms.ValidationError(
	# 			u'Empty text', code=1)
	 	return text
		
	def save(self):
		#question = Question(**self.cleaned_data)
		title = self.cleaned_data['title']
		text = self.cleaned_data['text']
		question = Question(title=title, text=text, author=self._user)
		question.save()
		return question		

class AnswerForm(forms.Form):
	text = forms.CharField(label="Asnwer:", widget=forms.Textarea, required=True)
	question = forms.IntegerField(widget=forms.HiddenInput, required=True)		
		
	def clean_text(self):
		text = self.cleaned_data['text']
	# 	if len(title) == 0:
	# 		raise forms.ValidationError(
	# 			u'Empty text', code=1)
	 	return text

	# def clean_question(self):
	# 	question = self.cleaned_data['question']
	# 	try:
	# 		question = int(question)
	# 	except:
	# 		forms.ValidationError(u'Question should be integer', code=1)
	#	return question

	# def clean(self):
	# 	return True

	def save(self):
		question_id = self.cleaned_data['question']
		data = {'text': self.cleaned_data['text'],
				#'question': Question.objects.get(pk=question_id),
				'question_id': int(question_id),
				'author': self._user
		}		
		#answer = Answer(**self.cleaned_data)
		answer = Answer(**data)
		answer.save()
		return answer	

class SignupForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'password')

	def save(self):
		user = User.objects.create_user(**self.cleaned_data)
		return user

class LoginForm(forms.Form):

	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput, required=True)
