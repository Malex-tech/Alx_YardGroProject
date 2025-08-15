from django.urls import path
from .views import ReportsListCreateView
from rest_framework.routers import DefaultRouter
from .views import ReportsViewSet

router = DefaultRouter()
router.register('', ReportsViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', ReportsListCreateView.as_view(), name='produce-list-create'),
]
