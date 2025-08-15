from rest_framework import generics
from .models import Produce
from .serializers import ProduceSerializer

class ProduceListCreateView(generics.ListCreateAPIView):
    queryset = Produce.objects.all()
    serializer_class = ProduceSerializer
