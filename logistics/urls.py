from django.urls import path
from .views import LogisticsListCreateView
from rest_framework.routers import DefaultRouter
from .views import LogisticsViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'', LogisticsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = router.urls

urlpatterns = [
    path('', LogisticsListCreateView.as_view(), name='produce-list-create'),
]
