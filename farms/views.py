from django.shortcuts import render
from rest_framework import generics
from .models import Farm
from .serializers import FarmSerializer
from rest_framework import viewsets

class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
# Create your views here.
