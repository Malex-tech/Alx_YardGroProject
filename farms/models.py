from django.db import models
from django.conf import settings

class Farm(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='farms')
    farm_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # hectares
    produce_types = models.TextField(help_text="Comma-separated list")

    def __str__(self):
        return f"{self.farm_name} ({self.owner.username})"
