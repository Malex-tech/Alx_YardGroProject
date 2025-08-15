from django.db import models
from farms.models import Farm

class Produce(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('pending', 'Pending'),
    )
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name='produce')
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)  # tons/kg
    price = models.DecimalField(max_digits=10, decimal_places=2)
    harvest_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.name} ({self.farm.farm_name})"
