from django.db import models
from django.urls import reverse

# Create your models here.

class Coin(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  face_value = models.FloatField('Face Value')
  appraised_value = models.FloatField('Appraised Value')
  notes = models.TextField(max_length=300)
    
  def get_appreciation_percentage(self):
    return self.appraised_value / self.face_value
  
  def __str__(self):
    return f'{self.year} - {self.title}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'coin_id': self.id})

  