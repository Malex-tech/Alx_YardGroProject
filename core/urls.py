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
from rest_framework.routers import DefaultRouter
from .views import home
# Import your viewsets
from farms.views import FarmViewSet
from produce.views import ProduceViewSet
from logistics.views import LogisticsViewSet
from delivery.views import DeliveryViewSet, delivery_list_page, delivery_form_page
from reports.views import ReportViewSet, report_list_page, report_form_page
from django.conf import settings
from rest_framework.settings import api_settings

# DRF Router handles all endpoints automatically
router = DefaultRouter()
router.register('farms', FarmViewSet, basename='farm')
router.register('produce', ProduceViewSet, basename='produce')
router.register('logistics', LogisticsViewSet, basename='logistics')
router.register('deliveries', DeliveryViewSet, basename='delivery')
router.register('reports', ReportViewSet, basename='report')
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),

    # API routes
    path('api/', include(router.urls)),
    path('api/', include('users.urls')), 
    path('api/farms/', include('farms.urls')),
    path('api/produce/', include('produce.urls')),
    path('api/logistics/', include('logistics.urls')),
    path('api/deliveries/', include('delivery.urls')),
    path('api/reports/', include('reports.urls')),
    path('api/users/', include('users.urls')),

    # Template pages
    path('deliveries/page/', delivery_list_page, name='delivery_list_page'),
    path('deliveries/new/', delivery_form_page, name='delivery_form_page'),
    path('reports/page/', report_list_page, name='report_list_page'),
    path('reports/new/', report_form_page, name='report_form_page'),

    # authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="YardGro API",
        default_version='v1',
        description="API documentation for YardGro",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]