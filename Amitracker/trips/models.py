from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser  # Import the User model from Django's authentication system


# Create your models here.


class Vehicle(models.Model):
    vehicle_type = models.CharField(max_length=50, blank=True, default='')
    vehicle_identifier = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Driver(models.Model):
    name = models.CharField(max_length=100, default='Tom')
    email = models.EmailField(default='Driver@test.com')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

class Customer(models.Model):
    name = models.CharField(max_length=100, default='Customer')
    email = models.EmailField(default='customer@test.com')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']



class Trips(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Reference to Vehicle model
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Reference to Customer model
    address = models.CharField(max_length=100, default='Nairobi')
    cargo_tonnage = models.DecimalField(max_digits=10, decimal_places=2) 
    address_type = models.CharField(choices=[('pickup', 'pickup_point'), ('drop', 'drop_off_point')], default='pickup', max_length=100)
    done_by_user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the User model for logged-in user
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']



class CustomUser(AbstractUser):
    # Your CustomUser fields here

    # Specify unique related_name values for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


