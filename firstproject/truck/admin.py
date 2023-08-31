from django.contrib import admin
from .models import TruckData

class TruckDataAdmin(admin.ModelAdmin):
    list_display=('license_plate','driver_name', 'checkin_manager', 'checkin_at')
admin.site.register(TruckData,TruckDataAdmin)

