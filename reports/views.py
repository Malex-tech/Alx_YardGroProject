from rest_framework import generics
from .models import Report
from .serializers import ReportSerializer

# Create and list reports
class ReportListCreateView(generics.ListCreateAPIView):
    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer

# Retrieve, update, or delete a single report
class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
