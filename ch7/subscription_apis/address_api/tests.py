from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Address


class AddressTests(APITestCase):
    url = 'http://127.0.0.1:7000/api/v1/addresses/'

    def test_create_address(self):

        data = {"name": "A. Anderson",
                "address": "Down Under 1",
                "postalcode": "ZPT 1",
                "city": "Gotham",
                "country": "Northland",
                "email": "anderson@upside.com"
                }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().name, 'A. Anderson')

    def test_create_address_postalcode_max(self):
        data = {"name": "B. Botir",
                "address": "Down Under 1",
                "postalcode": "ABCDEFGHIJ12345",
                "city": "Gotham",
                "country": "Northland",
                "email": "botir@upside.com"
                }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)
        self.assertEqual(Address.objects.get().name, 'B. Botir')

    def test_create_address_postalcode_too_long(self):
        data = {"name": "C. Chai",
                "address": "Down Under 1",
                "postalcode": "ABCDEFGHIJ123456",
                "city": "Gotham",
                "country": "Northland",
                "email": "chai@upside.com"
                }
        response = self.client.post(self.url, data, format='json')
        response.render()
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.content, b'{"postalcode":["Ensure this field has no more than 15 characters."]}')
