from django.http import HttpResponse


def hello(request):# все ф-ии -обработчики принимают аргумет request (тот кот. нам генерит браузер)
    return HttpResponse('<h1> Hello)<h1>')
