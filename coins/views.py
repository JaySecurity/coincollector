from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Coin


def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def coins_index(request):
  coins = Coin.objects.all()
  return render(request, 'coins/index.html', {'coins': coins})

def coins_detail(request, coin_id):
  coin = Coin.objects.get(id =  coin_id)
  return render(request, 'coins/detail.html', {'coin': coin})


class CoinCreate(CreateView):
  model = Coin
  fields = '__all__'

class CoinUpdate(UpdateView):
  model = Coin
  fields = '__all__'

class CoinDelete(DeleteView):
  model = Coin
  success_url = reverse_lazy('index')

