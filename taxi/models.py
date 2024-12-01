from django.db import models

class Taxi(models.Model):
    STATUS = [
        ('available', 'Available'),
        ('busy', 'Busy'),
        ('under maintenance', 'Under Maintenance'),
    ]
    taxi_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=100)
    driver_name = models.CharField(max_length=100)
    passenger_capacity = models.IntegerField()
    car_model = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS)
