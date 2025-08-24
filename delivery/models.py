from django.db import models
from django.conf import settings
from farms.models import Farm
from produce.models import Produce
from logistics.models import Logistics

class Delivery(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Requested'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE, related_name='deliveries')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchases')
    transporter = models.ForeignKey(Logistics, on_delete=models.CASCADE, related_name='deliveries')
    pickup_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='requested')
    eta = models.DateTimeField(null=True, blank=True)
    distance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   # reports/models.py
class Report(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    report_type = models.CharField(max_length=50)
    content = models.TextField()
   
    def __str__(self):
        return f"Delivery of {self.produce.name} to {self.buyer.username}"
