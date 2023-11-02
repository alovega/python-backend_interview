from rest_framework import serializers
from .models import Vehicle, Driver, Customer, Trips
import secrets

from django.contrib.auth import get_user_model


def generate_unique_api_token():
    return secrets.token_hex(20)
    
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']  # Add more fields as needed

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data, password=password)
        # Generate and save API token
        user.api_token = generate_unique_api_token()  # Implement generate_unique_api_token() function
        user.save()

        return user

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['vehicle_type', 'vehicle_identifier']

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['name', 'email']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'email']

class TripsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trips
        fields = '__all__'