from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Anunt
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    context = {
        'anunturi': Anunt.objects.all()
    }
    return render(request, 'anunt/home.html', context)


class AnuntListView(ListView):
    model = Anunt
    template_name = 'anunt/home.html'
    context_object_name = 'anunturi'
    ordering = ['-data_postarii']

class AnuntDetailView(DetailView):
    model = Anunt


class AnuntCreateView(LoginRequiredMixin, CreateView):
    model = Anunt
    fields = ['titlu', 'descriere']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)
    

class AnuntUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Anunt
    fields = ['titlu', 'descriere']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        anunt = self.get_object()
        if self.request.user == anunt.autor:
            return True
        return False

class AnuntDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Anunt
    success_url = '/'

    def test_func(self):
        anunt = self.get_object()
        if self.request.user == anunt.autor:
            return True
        return False
   

def about(request):
    return render(request, 'anunt/about.html', {'title': 'About'})



