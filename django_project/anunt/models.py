from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Model anunt
class Anunt(models.Model):
    titlu = models.CharField(max_length=200)
    descriere = models.TextField()
    data_postarii = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titlu

    def get_absolute_url(self):
        return reverse('anunt-detail', kwargs={'pk': self.pk})
