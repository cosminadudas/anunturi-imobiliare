from django.shortcuts import render
from .models import Anunt

def home(request):
    context = {
        'anunturi': Anunt.objects.all()
    }
    return render(request, 'anunt/home.html', context)

def about(request):
    return render(request, 'anunt/about.html', {'title': 'About'})



