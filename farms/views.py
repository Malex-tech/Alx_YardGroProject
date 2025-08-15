from django.shortcuts import render
from rest_framework import generics
from .models import Farm
from .serializers import FarmSerializer

class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

# Create your views here.
