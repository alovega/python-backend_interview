from django.urls import path
from .views import VehicleCreateView, CustomerCreateView, DriverCreateView, TripsCreateView, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Other URL patterns
    
    # URL pattern for creating a vehicle
    path('vehicle/create/', VehicleCreateView.as_view(), name='vehicle-create'),
    
    # URL pattern for creating a customer
    path('customer/create/', CustomerCreateView.as_view(), name='customer-create'),
    
    # URL pattern for creating a driver
    path('driver/create/', DriverCreateView.as_view(), name='driver-create'),

    # URL pattern for creating a trip
    path('trips/create/', TripsCreateView.as_view(), name='trips-create'),

    # URL pattern for user registration
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('api-token/', obtain_auth_token, name='api_token_auth'),
]
