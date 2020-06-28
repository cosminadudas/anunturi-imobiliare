from django.shortcuts import render

def home(request):
    return render(request, 'anunt/home.html')

def about(request):
    return render(request, 'anunt/about.html')
