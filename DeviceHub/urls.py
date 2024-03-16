from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CompanyViewSet, CheckoutViewSet, EmployeeViewSet, DeviceViewSet

router = DefaultRouter()
router.register(prefix="company", viewset=CompanyViewSet, basename="company")
router.register(prefix="employee", viewset=EmployeeViewSet, basename="employee")
router.register(prefix="device", viewset=DeviceViewSet, basename="device")
router.register(prefix="checkout", viewset=CheckoutViewSet, basename="checkout")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]
