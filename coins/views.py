import uuid

import boto3
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import AppraisalForm
from .models import Coin, Photo

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'coincollector2021'

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

@login_required
def coins_index(request):
  coins = Coin.objects.filter(user = request.user)
  return render(request, 'coins/index.html', {'coins': coins})

@login_required
def coins_detail(request, coin_id):
  coin = Coin.objects.get(id =  coin_id)
  app_form = AppraisalForm()
  return render(request, 'coins/detail.html', {'coin': coin, 'appraisal_form': app_form})

@login_required
def add_appraisal(request, coin_id):
  form = AppraisalForm(request.POST)
  if form.is_valid():
    new_appraisal = form.save(commit=False)
    new_appraisal.coin_id = coin_id
    new_appraisal.save()
  return redirect('detail', coin_id=coin_id)

@login_required
def add_photo(request, coin_id):
  photo_file = request.FILES.get('photo-file',None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file,BUCKET,key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, coin_id=coin_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', coin_id=coin_id)



class CoinCreate(LoginRequiredMixin, CreateView):
  model = Coin
  fields = '__all__'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class CoinUpdate(LoginRequiredMixin, UpdateView):
  model = Coin
  fields = '__all__'

class CoinDelete(LoginRequiredMixin,DeleteView):
  model = Coin
  success_url = reverse_lazy('index')


def signup(request):
  error_message = ''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid:
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = "Invalid Entry!"
  form = UserCreationForm
  context = {'form':form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
