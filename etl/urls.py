from django.urls import path

from . import views

urlpatterns = [
    path('', views.CsvDataListView.as_view(), name='csvdata_list')
]