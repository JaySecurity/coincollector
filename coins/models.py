from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

class Coin(models.Model):
  title = models.CharField(max_length=100)
  year = models.IntegerField()
  face_value = models.FloatField('Face Value')
  notes = models.TextField(max_length=300)

  @property
  def appraised_value(self):
    return self.appraisal_set.last().value
      
  def get_appreciation_percentage(self):
    return self.appraisal_set.last().value / self.face_value
  
  def __str__(self):
    return f'{self.year} - {self.title}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'coin_id': self.id})

class Appraisal(models.Model):
  date = models.DateField()
  value = models.FloatField()
  coin = models.ForeignKey(Coin, on_delete = models.CASCADE)

  def __str__(self):
    return f"Appraised for {self.value} on {self.date}"
