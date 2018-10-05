from django.db import models
from django.urls import reverse


class CsvData(models.Model):
    name = models.CharField(max_length=31)
    ipv4 = models.GenericIPAddressField()
    mac_address = models.CharField(max_length=17)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name + " - " + self.ipv4

    def get_absolute_url(self):
        return reverse('etl_csvdata_detail', args=(self.id, ))

    def get_update_url(self):
        return reverse('etl_csvdata_update', args=(self.id, ))