from rest_framework import generics
from .models import Logistics
from .serializers import LogisticsSerializer

class ProduceListCreateView(generics.ListCreateAPIView):
    queryset = Logistics.objects.all()
    serializer_class = LogisticsSerializer
