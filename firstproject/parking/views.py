from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import ViolatorData, EmployeeOfMonthData, CarData
from datetime import datetime

# Create your views here.
@login_required
def PhomeView(request):
    return render(request, 'parking/parking_home.html')

@login_required
def PviolatorView(request):
    if request.method=='POST':
        get_location=request.POST.get('location')

        get_plate=request.POST.get('plate')
        get_plate_front=str(get_plate).lstrip()
        get_plate_back=str(get_plate_front).strip()
        get_plate_middle=str(get_plate_back).replace(" ","")
        get_plate=get_plate_middle

        recent_data=ViolatorData.objects.filter(car_plate=get_plate, parking_lot=get_location).order_by('-parking_at').first()
        if recent_data:
            previous_count=recent_data.violate_count
            plate_count=previous_count+1
        else:
            plate_count=1
        data_add=ViolatorData(car_plate=get_plate, parking_lot=get_location, violate_count=plate_count)
        data_add.save()
        return render(request, 'parking/violator_list.html')
    return render(request, 'parking/violator.html')

@login_required
def PviolatorlistView(request):
    violator_list=ViolatorData.objects.all()
    context={
        'violator_list':violator_list
    }
    return render(request, 'parking/violator_list.html', context)

@login_required
def PviolatordeleteView(request, data_id):
    if request.method=='POST':
        selected_data=ViolatorData.objects.get(pk=data_id)
        selected_data.delete()
    return redirect('parking/violator_list_url')

@login_required
def PemployeeView(request):
    if request.method=='POST':
        get_name=request.POST.get('name')
        get_date=request.POST.get('date')
        get_to_date=get_date.split('to')
        start_strip=get_to_date[0].lstrip()
        end_strip=get_to_date[1].strip()
        get_start=datetime(int(start_strip[:4]),int(start_strip[5:7]),int(start_strip[8:10]))
        get_end=datetime(int(end_strip[:4]),int(end_strip[5:7]),int(end_strip[8:10]))
        data_add=EmployeeOfMonthData(employee_name=get_name, start_date=get_start, end_date=get_end)
        data_add.save()
        return render(request, 'parking/employee_list.html')
    return render(request, 'parking/employee.html')

@login_required
def PemployeelistView(request):
    employee_list=EmployeeOfMonthData.objects.all()
    context={
        'employee_list':employee_list
    }
    return render(request, 'parking/employee_list.html', context)
