from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import IdData
from datetime import datetime
from django.utils import timezone

# Create your views here.
@login_required
def VhomeView(request):
    return render(request, 'visitor/visitor_home.html')

@login_required
def VregisterView(request):
    if request.method=='POST':
        get_name=request.POST.get('name')
        get_company=request.POST.get('company')
        get_date=request.POST.get('date')
        get_purpose=request.POST.get('purpose')
        get_laptop=request.POST.get('laptop')
        get_pic=request.POST.get('pic')
        get_remark=request.POST.get('remark')
        get_to_date=get_date.split('to')
        start_strip=get_to_date[0].lstrip()
        end_strip=get_to_date[1].strip()
        get_start=datetime(int(start_strip[:4]),int(start_strip[5:7]),int(start_strip[8:10]))
        get_end=datetime(int(end_strip[:4]),int(end_strip[5:7]),int(end_strip[8:10]))
        
        visitor_add=IdData(visitor_name=get_name, visitor_company=get_company, start_date=get_start, end_date=get_end, visitor_purpose=get_purpose, bring_laptop=get_laptop, pic=get_pic, remark=get_remark, user=request.user)
        visitor_add.save()
        return redirect('Vmyapproval_url')
    return render(request, 'visitor/register.html')

@login_required
def VmyView(request):
    #if there is no contents -> no sending to templates
    try:
        visitor_mylist=IdData.objects.filter(user=request.user).order_by('-id')
        context={
            'visitor_mylist':visitor_mylist
        }
        return render(request, 'visitor/myapproval.html', context)
    # if there is contents
    except:
        return render(request, 'visitor/myapproval.html')

@login_required
def VlistView(request):
    try:
        visitor_list=IdData.objects.all().order_by('-id')
        context={
            'visitor_list':visitor_list
        }
        return render(request, 'visitor/visitorlist.html', context)
    except:
        return render(request,'visitor/visitorlist.html')

@login_required
def VdeleteView(request, data_id):
    if request.method=='POST':
        selected_data=IdData.objects.get(pk=data_id)
        selected_data.delete()
        previous_page=request.META.get('HTTP-REFERER','/')
    return redirect(previous_page)

@login_required
def VmydeleteView(request, data_id):
    if request.method=='POST':
        selected_data=IdData.objects.get(pk=data_id)
        selected_data.delete()
        print(data_id)
    return redirect('Vmyapproval_url')

@login_required
def VlistdeleteView(request, data_id):
    if request.method=='POST':
        try:
            selected_data=IdData.objects.get(pk=data_id)
            selected_data.delete()
        except IdData.DoesNotExist:
            pass
    return redirect('Vlist_url')


@login_required
def VtogglemyView(request, data_id):
    if request.method=='POST':
        visitor=get_object_or_404(IdData, id=data_id)
        visitor.show_remark=not visitor.show_remark
        visitor.save()
        return redirect('Vmyapproval_url')

@login_required
def VtogglelistView(request, data_id):
    if request.method=='POST':
        visitor=get_object_or_404(IdData, id=data_id)
        visitor.show_remark=not visitor.show_remark
        visitor.save()
        return redirect('Vlist_url')

@login_required
def VapprovalView(request, data_id):
    if request.method=="POST":
        approve_data=IdData.objects.get(id=data_id)
        approve_data.security_approval=timezone.now()
        approve_data.save()
        return redirect('Vlist_url')

@login_required
def VpassView(request, data_id):
    if request.method=='POST':
        parking_data=IdData.objects.get(id=data_id)
        return render(request, 'visitor/parkingpass.html', {'parking_list':parking_data})

@login_required
def VcheckinView(request, data_id):
    if request.method=="POST":
        checkin_data=IdData.objects.get(id=data_id)
        checkin_data.check_in=timezone.now()
        checkin_data.save()
        return redirect('Vlist_url')

@login_required
def VcheckoutView(request, data_id):
    if request.method=="POST":
        checkout_data=IdData.objects.get(id=data_id)
        checkout_data.check_out=timezone.now()
        checkout_data.save()
        return redirect('Vlist_url')  