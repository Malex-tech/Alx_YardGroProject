from django.urls import path
from .views import DeliveryListCreateView
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet

router = DefaultRouter()
router.register('', FarmViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', DeliveryListCreateView.as_view(), name='produce-list-create'),
]
