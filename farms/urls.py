from django.urls import path
from .views import FarmListCreateView

urlpatterns = [
    path('', FarmListCreateView.as_view(), name='farm-list-create'),
]
