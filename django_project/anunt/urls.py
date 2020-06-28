from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name= 'anunt-home'),
    path('about/', views.about, name= 'anunt-about'),
]