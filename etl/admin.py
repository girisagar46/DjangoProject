from django.contrib import admin

from .models import CsvData


class CsvDataAdmin(admin.ModelAdmin):
    list_display = ['name', 'ipv4', 'mac_address']
    list_display_links = ['ipv4', 'name']


admin.site.register(CsvData, CsvDataAdmin)
