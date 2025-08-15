from rest_framework import generics
from .models import Reports
from .serializers import ReportsSerializer
from rest_framework import viewsets

class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer

class ProduceListCreateView(generics.ListCreateAPIView):
    queryset = Reports.objects.all()
    serializer_class = ReportsSerializer