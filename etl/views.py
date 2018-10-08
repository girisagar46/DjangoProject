from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .models import CsvData
from .forms import CsvDataForm


# class CsvDataView(View):
#     template_name = 'etl/csvdata_list.html'
#
#     def get(self, request, *args, **kwargs):
#         csv_data = CsvData.objects.all()
#         return render(request, self.template_name, {"csv_data": csv_data})

class CsvDataListView(ListView):
    model = CsvData


class CsvDataCreateView(CreateView):
    model = CsvData
    form_class = CsvDataForm

class CsvDataDetailView(DetailView):
    model = CsvData

class CsvDataUpdateView(UpdateView):
    model = CsvData
    form_class = CsvDataForm