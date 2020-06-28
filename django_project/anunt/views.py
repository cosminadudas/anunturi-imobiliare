from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Anunt home</h1>')

def about(request):
    return HttpResponse('<h1>Anunt about</h1>')
