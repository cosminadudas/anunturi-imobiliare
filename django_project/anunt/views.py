from django.shortcuts import render

anunturi = [
    {
        'autor' : 'Cosmina',
        'titlu' : 'Anunt apartament 1',
        'descriere' : 'Primul apartament de vanzare',
        'data_postarii' : 'Iunie 28, 2020'
    },
    {
        'autor' : 'David',
        'titlu' : 'Anunt apartament 2',
        'descriere' : 'Al doilea apartament de vanzare',
        'data_postarii' : 'Iunie 29, 2020'
    }
]


def home(request):
    context = {
        'anunturi': anunturi
    }
    return render(request, 'anunt/home.html', context)

def about(request):
    return render(request, 'anunt/about.html', {'title': 'About'})
