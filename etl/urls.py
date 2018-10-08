from django.urls import path

from . import views

urlpatterns = [
    path('', views.CsvDataListView.as_view(), name='csvdata_list'),
    path('create/', views.CsvDataCreateView.as_view(), name='csvdata_create'),
    path('detail/<int:pk>', views.CsvDataDetailView.as_view(), name='etl_csvdata_detail'),
    path('update/<int:pk>', views.CsvDataUpdateView.as_view(), name='etl_csvdata_update')
]