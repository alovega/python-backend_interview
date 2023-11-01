from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from trips.models import Vehicle, Customer, Driver, Trips
from trips.serializers import VehicleSerializer, CustomerSerializer, DriverSerializer, TripsSerializer

class VehicleCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vehicle_data = {'vehicle_type': 'Car', 'vehicle_identifier': '123'}
        self.url = reverse('vehicle-create')

    def test_create_vehicle(self):
        response = self.client.post(self.url, self.vehicle_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 1)
        vehicle = Vehicle.objects.get()
        self.assertEqual(vehicle.vehicle_type, 'Car')

class CustomerCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.customer_data = {'name': 'John Doe', 'email': 'john@example.com'}
        self.url = reverse('customer-create')

    def test_create_customer(self):
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        customer = Customer.objects.get()
        self.assertEqual(customer.name, 'John Doe')

class DriverCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.driver_data = {'name': 'Alice', 'email': 'alice@example.com'}
        self.url = reverse('driver-create')

    def test_create_driver(self):
        response = self.client.post(self.url, self.driver_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Driver.objects.count(), 1)
        driver = Driver.objects.get()
        self.assertEqual(driver.name, 'Alice')

class TripsCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.trips_data = {
            'vehicle_id': {'vehicle_type': 'Car', 'vehicle_identifier': '123'},
            'customer_id': {'name': 'John Doe', 'email': 'john@example.com'},
            'address': 'Test Address',
            'cargo_tonnage': 5.0,
            'address_type': 'pickup',
            'done_by_user': 'testuser'
        }
        self.url = reverse('trips-create')

    def test_create_trips(self):
        response = self.client.post(self.url, self.trips_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Trips.objects.count(), 1)
        trips = Trips.objects.get()
        self.assertEqual(trips.address, 'Test Address')
