import datetime
from django.shortcuts import render


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