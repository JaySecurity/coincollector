from django.shortcuts import render

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
