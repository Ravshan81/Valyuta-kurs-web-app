from django.shortcuts import render
import requests

def KursView(request):
    url = 'https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/latest/USD'
    response = requests.get(url).json()
    dollar = response['conversion_rates']['UZS']
    url2 = 'https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/latest/RUB'
    response1 = requests.get(url2).json()
    rubl = response1['conversion_rates']['UZS']
    url3 = 'https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/latest/EUR'
    response3 = requests.get(url3).json()
    euro = response3['conversion_rates']['UZS']

    context = {
        'dollar': dollar,
        'rubl': rubl,
        'euro': euro
    }

    return render(request, 'index.html', context)
