from django.urls import path
from .views import ProduceListCreateView

urlpatterns = [
    path('', ProduceListCreateView.as_view(), name='produce-list-create'),
]
