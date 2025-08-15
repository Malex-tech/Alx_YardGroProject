from django.db import models
from django.conf import settings

class Logistics(models.Model):
    transporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='logistics')
    vehicle_type = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # tons/kg
    availability = models.BooleanField(default=True)
    route = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.vehicle_type} ({self.transporter.username})"
