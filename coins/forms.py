from django.forms import ModelForm
from .models import Appraisal

class AppraisalForm(ModelForm):
  class Meta:
    model = Appraisal
    fields = ['date', 'value']