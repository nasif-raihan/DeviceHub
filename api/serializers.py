from rest_framework import serializers

from .models import Checkout, Company, Device, Employee


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    employees = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = "__all__"

    @staticmethod
    def get_employees(obj):
        employees = Employee.objects.filter(company=obj)
        return EmployeeSerializer(employees, many=True).data

    def create(self, validated_data):
        employees = validated_data.pop("employee")
        model_instance = Company.objects.create(**validated_data)

        for employee in employees:
            Employee.objects.create(model_instance, **employee)
        return model_instance


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
