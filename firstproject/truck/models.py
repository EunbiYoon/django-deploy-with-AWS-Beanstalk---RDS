from django.db import models

# Create your models here.
class TruckData(models.Model):
    checkin_at=models.DateTimeField(null=True)
    checkin_manager=models.CharField(max_length=255, null=True)
    driver_name=models.CharField(max_length=255, null=True)
    license_plate=models.CharField(max_length=255, null=True)
    company_name=models.CharField(max_length=255, null=True)
    truck_number=models.CharField(max_length=255, null=True)
    direct_cntr=models.CharField(max_length=255, null=True)
    in_trailer=models.CharField(max_length=255, null=True)
    seal_number=models.CharField(max_length=255, null=True)
    
    checkout_at=models.DateTimeField(blank=True, null=True)
    checkout_manager=models.CharField(max_length=255, null=True)
    out_trailer=models.CharField(max_length=255, null=True)
    load_status=models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.license_plate)
    class Meta:
        verbose_name_plural='Truck Tracking Data'

