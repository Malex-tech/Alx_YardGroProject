from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('buyer', 'Buyer'),
        ('logistics', 'Logistics Partner'),
        ('agent', 'Delivery Agent'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    location = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
