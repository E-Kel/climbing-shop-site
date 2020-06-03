from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts_lists(request):
    return HttpResponse('<h1> Heeey!</h1>')
