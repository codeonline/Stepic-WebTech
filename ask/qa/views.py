# coding=utf-8
from django.shortcuts import render, get_object_or_404
# from django.http import Http404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage
#from ask.qa.models import *
from qa.models import *

# Create your views here.
from django.http import HttpResponse


@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


# URL = /?page=2
#
# Главная страница.
# Список "новых" вопросов. Т.е. последний заданный вопрос - первый в списке.
# На этой странице должна работать пагинация.
# Номер страницы указывается в GET параметре page.
# На страницу выводится по 10 вопросов.
# В списке вопросов должны выводится заголовки (title) вопросов и
# ссылки на страницы отдельных вопросов.

@require_GET
def main_page(request):
    questions = Question.objects.order_by('-added_at').all()
    #questions.order_by('-added_at')   
    limit = 10
    paginator = Paginator(questions, limit)

    try:
        page_num = int(request.GET.get('page', 1))
    except ValueError:
        page_num = 1

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'main_page.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


# URL = /popular/?page=3
#
# Cписок "популярных" вопросов.
# Сортировка по убыванию поля rating.
# На этой странице должна работать пагинация.
# Номер страницы указывается в GET параметре page.
# На страницу выводится по 10 вопросов.
# В списке вопросов должны выводится заголовки (title) вопросов и
# ссылки на страницы отдельных вопросов.
@require_GET
def popular(request):
    questions = Question.objects.order_by('-rating').all()
    #questions.order_by('-rating')
    limit = 10
    paginator = Paginator(questions, limit)

    try:
        page_num = int(request.GET.get('page', 1))
    except ValueError:
        page_num = 1

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


# URL = /question/5/
#
# Страница одного вопроса.
# На этой странице должны выводится заголовок (title), текст (text) вопроса и
# все ответы на данный вопрос, без пагинации.
# В случае неправильного id вопроса view должна возвращать 404.
@require_GET
def question(request, id):
    q = get_object_or_404(Question, pk=id)
    return render(request, 'question.html', {
        'question': q,
    })
