from rest_framework import serializers

from .models import Checkout, Company, Device, Employee


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    device = DeviceSerializer(many=True)

    class Meta:
        model = Employee
        fields = "__all__"

    def create(self, validated_data):
        devices = validated_data.pop("device")
        model_instance = Employee.objects.create(**validated_data)

        for device in devices:
            Device.objects.create(model_instance, **device)
        return model_instance


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"
