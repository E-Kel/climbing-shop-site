from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def posts_lists(request):
    n = "Jenya"
    m = ["Jenya", "Vasya", "Petya", "Olja"]
    return render(request, "blog/index.html", context={"name":n, "names":m})#все ключи словаря context - эьто те ключи которые будут использвоаны в шаблоне
