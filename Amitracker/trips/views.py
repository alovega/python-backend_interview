from rest_framework import generics
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .models import Trips, Customer, Vehicle, Driver
from .custom_auth import NoAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from .serializers import TripsSerializer, DriverSerializer, CustomerSerializer, VehicleSerializer, UserRegistrationSerializer

class TripsCreateView(generics.CreateAPIView):
    queryset = Trips.objects.all()
    serializer_class = TripsSerializer
    authentication_classes = [TokenAuthentication]
    

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'status_code': status.HTTP_201_CREATED,
                'status': 'Created',
                'description': 'Trip created successfully.'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'status': 'Bad Request',
                'description': 'Invalid data provided. Please check your input.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class VehicleCreateView(generics.CreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'status_code': status.HTTP_201_CREATED,
                'status': 'Created',
                'description': 'Vehicle created successfully.'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'status': 'Bad Request',
                'description': 'Invalid data provided. Please check your input.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)

class CustomerCreateView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'status_code': status.HTTP_201_CREATED,
                'status': 'Created',
                'description': 'Customer created successfully.'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'status': 'Bad Request',
                'description': 'Invalid data provided. Please check your input.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


class DriverCreateView(generics.CreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            response_data = {
                'status_code': status.HTTP_201_CREATED,
                'status': 'Created',
                'description': 'Driver created successfully.'
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            response_data = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'status': 'Bad Request',
                'description': 'Invalid data provided. Please check your input.'
            }
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = [NoAuthentication]
    throttle_classes = [UserRateThrottle]

    def create(self, request, *args, **kwargs):
        response = super(UserRegistrationView, self).create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            user = response.data
            token, created = Token.objects.get_or_create(user=user)
            response.data['token'] = token.key
        return response