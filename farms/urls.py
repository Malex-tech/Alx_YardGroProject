from django.urls import path
from .views import FarmListCreateView
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('farms', FarmViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls)),
    path('', FarmListCreateView.as_view(), name='farm-list-create'),
]
