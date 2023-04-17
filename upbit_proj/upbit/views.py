from django.shortcuts import render
from django.http import JsonResponse
from .models import CoinData

def index(request):
    return render(request, 'index.html')


def get_coin_data(request):
    data = CoinData.objects.latest(id)
    return JsonResponse({
        'opening_price': data.opening_price,
        'high_price': data.high_price,
        'low_price': data.low_price,
        'trade_price': data.trade_price,
    })
