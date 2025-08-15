from rest_framework import serializers
from .models import Logistics

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logistics
        fields = '__all__'
