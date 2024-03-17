from djongo import models


class Address(models.Model):
    name = models.CharField(max_length=120, blank=True)
    address = models.CharField(max_length=120, blank=True)
    postalcode = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=120, blank=True)
    country = models.CharField(max_length=80, blank=True)
    email = models.EmailField(blank=True)

class Magazine(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=500, blank=True)