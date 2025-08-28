from django.contrib import admin
from .models import Logistics
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(Logistics)
class LogisticsAdmin(admin.ModelAdmin):
    autocomplete_fields = ['transporter']

@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']
