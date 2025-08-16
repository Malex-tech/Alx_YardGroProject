from django.urls import path
from .views import DeliveryListCreateView
from rest_framework.routers import DefaultRouter
from .views import DeliveryViewSet

router = DefaultRouter()
router.register('', DeliveryViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', DeliveryListCreateView.as_view(), name='produce-list-create'),
]
