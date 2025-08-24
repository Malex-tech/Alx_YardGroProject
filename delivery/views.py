from rest_framework import generics
from .models import Delivery
from .serializers import DeliverySerializer
from rest_framework import viewsets
from rest_framework import viewsets, permissions

class DeliveryListCreateView(generics.ListCreateAPIView):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    
class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users see deliveries they are involved in
        user = self.request.user
        return Delivery.objects.filter(buyer=user) | Delivery.objects.filter(transporter__transporter=user)

# reports/views.py
from rest_framework import viewsets
from .models import Report
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user)