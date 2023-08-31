from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import TruckData
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
@login_required
def ThomeView(request):
    return render(request, 'truck/truck_home.html')

@login_required
def TcheckinView(request):
    if request.method=='POST':
        get_driver=request.POST.get('drivername')
        get_plate=request.POST.get('plate')
        get_company=request.POST.get('company')
        get_truck=request.POST.get('trucknumber')
        get_cntr=request.POST.get('cntr')
        get_trailer=request.POST.get('trailer')
        get_seal=request.POST.get('seal')

        data_add=TruckData(
                           driver_name=get_driver, license_plate=get_plate,
                           company_name=get_company, truck_number=get_truck,
                           direct_cntr=get_cntr, in_trailer=get_trailer,
                           seal_number=get_seal)
        data_add.checkin_manager=request.user
        data_add.checkin_at=timezone.now()
        data_add.save()
        truck_list=TruckData.objects.all().order_by('-checkin_at')
        context={
            'truck_list':truck_list
        }
        return render(request, 'truck/truck_history.html', context)
    return render(request,'truck/truck_in.html')

@login_required
def TcheckoutView(request):
    if request.method=='POST':
        get_outtrailer=request.POST.get('outtrailer')
        get_load=request.POST.get('load')
        data_add=TruckData(out_trailer=get_outtrailer, load_status=get_load)
        data_add.checkout_manager=request.user
        data_add.checkout_at=timezone.now()
        data_add.save()

        truck_list=TruckData.objects.all().order_by('-checkin_at')
        context={
            'truck_list':truck_list
        }
        return render(request, 'truck/truck_history.html', context)
    return render(request, 'truck/truck_out.html')

@login_required
def ThistoryView(request):
    truck_list=TruckData.objects.all().order_by('-checkin_at')
    context={
        'truck_list':truck_list
    }
    return render(request, 'truck/truck_history.html', context)