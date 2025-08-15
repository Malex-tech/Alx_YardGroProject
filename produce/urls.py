from django.urls import path
from .views import ProduceListCreateView
from rest_framework.routers import DefaultRouter
from .views import ProduceViewSet

router = DefaultRouter()
router.register('', ProduceViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('', ProduceListCreateView.as_view(), name='produce-list-create'),
]
