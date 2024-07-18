from django.db import models

class Price(models.Model):
    vehicle_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.vehicle_type}: {self.amount}'

class Addon(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}: {self.price}'

class Service(models.Model):
    name = models.CharField(max_length=100)
    includes = models.TextField()
    prices = models.ManyToManyField(Price)
    addons = models.ManyToManyField(Addon, blank=True)

    def __str__(self):
        return self.name
