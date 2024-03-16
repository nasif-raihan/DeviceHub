from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Checkout, Company, Device, Employee
from .serializers import (
    CompanySerializer,
    CheckoutSerializer,
    DeviceSerializer,
    EmployeeSerializer,
)


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class DeviceViewSet(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CheckoutViewSet(ModelViewSet):
    queryset = Checkout.objects.all()
    serializer_class = CheckoutSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
