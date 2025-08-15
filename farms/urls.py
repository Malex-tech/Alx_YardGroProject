from django.urls import path
from .views import FarmListCreateView
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet

router = DefaultRouter()
router.register('', FarmViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', FarmListCreateView.as_view(), name='farm-list-create'),
]
