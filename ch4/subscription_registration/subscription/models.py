from django.db import models


class Address(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=120)
    postalcode = models.CharField(max_length=20)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    email = models.EmailField()
