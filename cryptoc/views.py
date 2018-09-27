import datetime

import requests
from django.shortcuts import render

API_ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/?limit=10"


def currencies(request):
    response_data = requests.get(API_ENDPOINT)

    ctx = {
        "data": response_data.json()
    }

    return render(request,
                  template_name='cryptoc/currencies.html',
                  context=ctx)

def github(request):
    endpoint = "https://api.github.com/users/girisagar46"
    ctx = {
        "github_data": requests.get(endpoint).json()
    }

    return render(request, template_name='cryptoc/git.html', context=ctx)


def index(request):
    data = {
        "today_date": datetime.datetime.now()
    }

    return render(request,
                  template_name='cryptoc/crypto_index.html',
                  context=data)


def about(request):
    data = {
        "about_us": "This is a project for cryptocurrencies",
        "numbers": ["98073XXXXX", "980402XXXXX"]
    }

    return render(request,
                  template_name='cryptoc/about.html',
                  context=data)