from django.urls import path

from cryptoc.views import index, about, currencies, github

urlpatterns = [
    path('', index, name='crypto_index'),
    path('about/', about, name='crypto_about'),
    path('crypto/', currencies, name='crypto_currencies'),
    path('github/', github, name='github'),
]