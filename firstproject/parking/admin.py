from django.contrib import admin
from .models import ViolatorData,EmployeeOfMonthData, CarData

# Register your models here.
class ViolatorDataAdmin(admin.ModelAdmin):
    list_display=['car_plate','parking_at','violate_count']

admin.site.register(ViolatorData, ViolatorDataAdmin)


# Register your models here.
class EmployeeOfMonthDataAdmin(admin.ModelAdmin):
    list_display=['employee_name','register_at','start_date','end_date']

admin.site.register(EmployeeOfMonthData, EmployeeOfMonthDataAdmin)

# Register your models here.
class CarDataAdmin(admin.ModelAdmin):
    list_display=['visitor_name','visitor_company','visitor_car','park_location','start_date','end_date','register_at']
admin.site.register(CarData, CarDataAdmin)