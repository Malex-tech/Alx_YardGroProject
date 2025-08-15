from django.urls import path
from .views import LogisticsListCreateView

urlpatterns = [
    path('', LogisticsListCreateView.as_view(), name='produce-list-create'),
]
