from django.test import TestCase, Client
from django.urls import reverse


class CsvDataViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_list_csvdata(self):
        url = reverse("csvdata_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_csv_data(self):
        url = reverse("csvdata_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_data(self):
        url = reverse("csvdata_create")
        data = {
            "name": "Test Name",
            "ipv4": "192.168.0.1",
            "mac_address": "84:45:56:56:89:89:45"
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)







