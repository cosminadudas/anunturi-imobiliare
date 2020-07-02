from django.urls import path
from .views import AnuntListView, AnuntDetailView, AnuntCreateView, AnuntUpdateView, AnuntDeleteView
from . import views

urlpatterns = [
    path('', AnuntListView.as_view(), name= 'anunt-home'),
    path('anunt/<int:pk>/', AnuntDetailView.as_view(), name= 'anunt-detail'),
    path('anunt/new/', AnuntCreateView.as_view(), name= 'anunt-create'),
    path('anunt/<int:pk>/update', AnuntUpdateView.as_view(), name= 'anunt-update'),
    path('anunt/<int:pk>/delete', AnuntDeleteView.as_view(), name= 'anunt-delete'),
    path('about/', views.about, name= 'anunt-about'),
]