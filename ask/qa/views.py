from django.shortcuts import render

# Create your views here.
from dhango.http import HttpResponse
def test(request, *args, **kwargs):
    return HttpResponse('OK')
