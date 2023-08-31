from django.db import models

# Create your models here.
class ViolatorData(models.Model):
    car_plate=models.CharField(max_length=255)
    parking_lot=models.CharField(max_length=255)
    parking_at=models.DateTimeField(auto_now_add=True)
    violate_count=models.IntegerField(null=False, blank=False)

class EmployeeOfMonthData(models.Model):
    employee_name=models.CharField(max_length=255)
    register_at=models.DateTimeField(auto_now_add=True)
    start_date=models.DateTimeField(null=False, blank=False)
    end_date=models.DateTimeField(null=False, blank=False)

class CarData(models.Model):
    visitor_name=models.CharField(max_length=255, null=False, blank=False)
    visitor_company=models.CharField(max_length=255, null=False, blank=False)
    register_at=models.DateTimeField(auto_now_add=True)
    visitor_car=models.CharField(max_length=255, null=False, blank=False)
    park_location=models.CharField(max_length=255, null=False, blank=False)
    start_date=models.DateTimeField(null=False, blank=False)
    end_date=models.DateTimeField(null=False, blank=False)