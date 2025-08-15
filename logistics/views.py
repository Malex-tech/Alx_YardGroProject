from rest_framework import generics
from .models import Logistics
from .serializers import LogisticsSerializer
from rest_framework import viewsets

class LogisticsViewSet(viewsets.ModelViewSet):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer


class LogisticsListCreateView(generics.ListCreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
