"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from rest_framework.routers import DefaultRouter

# Import all your viewsets
from farms.views import FarmViewSet
from produce.views import ProduceViewSet
from logistics.views import LogisticsViewSet
from delivery.views import DeliveryViewSet
from reports.views import ReportViewSet

# DRF Router handles all endpoints automatically
router = DefaultRouter()
router.register('farms', FarmViewSet, basename='farm')
router.register('produce', ProduceViewSet, basename='produce')
router.register('logistics', LogisticsViewSet, basename='logistics')
router.register('deliveries', DeliveryViewSet, basename='delivery')
router.register('reports', ReportViewSet, basename='report')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')), 
    path('api/farms/', include('farms.urls')),
    path('api/produce/', include('produce.urls')),
    path('api/logistics/', include('logistics.urls')),
    path('api/deliveries/', include('delivery.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/users/', include('users.urls')).
    # All API endpoints from ViewSets
    path('api/', include(router.urls)),
]
