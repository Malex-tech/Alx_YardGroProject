from rest_framework import generics
from .models import Produce
from .serializers import ProduceSerializer
from rest_framework import viewsets

class ProduceViewSet(viewsets.ModelViewSet):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer

class ProduceListCreateView(generics.ListCreateAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer


