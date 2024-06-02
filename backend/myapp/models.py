# myapp/models.py
from django.db import models

class EnergyData(models.Model):
    name = models.CharField(max_length=100)
    energy_consumption = models.FloatField()
    renewable_availability = models.FloatField()
    fossil_fuel_usage = models.FloatField()
    cost = models.FloatField()
    
    def __str__(self):
        return self.name
