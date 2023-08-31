from django.shortcuts import render
from .models import QRCodeData
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required
def DhomeView(request):
    return render(request, 'delivery/delivery_home.html')


@login_required
def DsearchView(request):
    item_list=QRCodeData.objects.all()
    username=request.user.username
    context={
        'item_list':item_list,
        'username':username,
    }
    return render(request, 'delivery/search.html', context)

@login_required
def DsearchcheckoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        user_authority=request.user
        #remove input 4 digit space
        scan_track=scan_track.replace(" ","")
        #check code_data exist
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            admin_check_last=entry.admin_check
            user_check_last=entry.receiver_check
            # superuser
            if user_authority.is_superuser:
                if admin_check_last==True:
                    context={
                        "error":"Admin already checkout!"
                    }
                    return render(request,'delivery/msg_fail.html', context=context)
                else:
                    entry.admin_check=True
                    entry.admin_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Admin checkout successfully!",
                    }
                    return render(request,'delivery/msg_success.html', context=context)
            # staffuser
            else:
                if user_check_last==True:
                    context={
                        "error":"Receiver already checkout!"
                    }
                    return render(request,'delivery/msg_fail.html', context=context)
                else:
                    entry.receiver_check=True
                    entry.receiver_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Receiver checkout successfully!"
                    }
                    return render(request,'delivery/msg_success.html', context=context)
        except QRCodeData.DoesNotExist:
            context={
                "error":"Tracking number not exists!"
            }
            return render(request,'delivery/msg_fail.html', context=context)
    return render(request,'delivery/checkoutdelivery.html')


@login_required
def DcheckoutView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        user_authority=request.user
        user_name=request.user.username

        #remove input 4 digit space
        scan_track=scan_track.replace(" ","")

        #check code_data exist
        try:
            entry=QRCodeData.objects.get(code_data=scan_track)
            admin_check_last=entry.admin_check
            user_check_last=entry.receiver_check
            # superuser
            if user_authority.is_superuser:
                if admin_check_last==True:
                    context={
                        "error":"Admin already checkout!"
                    }
                    return render(request,'delivery/msg_fail.html', context=context)
                else:
                    entry.admin_check=True
                    entry.admin_at=timezone.now()
                    entry.save()
                    context={
                        "message":"Admin checkout successfully!",
                    }
                    return render(request,'delivery/msg_success.html', context=context)
            # staffuser
            else:
                if user_check_last==True:
                    context={
                        "error":"Receiver already checkout!"
                    }
                    return render(request,'delivery/msg_fail.html', context=context)
                else:
                    #check receiver and username matching
                    if user_name==entry.receiver:
                        entry.receiver_check=True
                        entry.receiver_at=timezone.now()
                        entry.save()
                        context={
                            "message":"Receiver checkout successfully!"
                        }
                        return render(request,'delivery/msg_success.html', context=context)
                    else:
                        context={
                            "error":"This is not your package!"
                        }
                        return render(request,'delivery/msg_fail.html', context=context)
        except QRCodeData.DoesNotExist:
            context={
                "error":"Tracking number not exists!"
            }
            return render(request,'delivery/msg_fail.html', context=context)
    return render(request,'delivery/checkoutdelivery.html')

@login_required
def DaddView(request):
    return render(request,'delivery/add.html')

@login_required
def DaddscanView(request):
    if request.method=='POST':
        scan_track=request.POST.get('result')
        #remove input 4 digit space
        scan_track=scan_track.replace(" ","")
        scan_receiver=request.POST.get('receiver')

        #if each colum empty
        if not scan_track:
            context={
                "error":"Tracking number is empty!"
            }
            return render(request,'delivery/msg_fail.html', context=context)
        elif not scan_receiver:
            context={
                "error":"Receiever is empty!"
            }
            return render(request,'delivery/msg_fail.html', context=context)
        #compare existed query
        else:
            entry_exists=QRCodeData.objects.filter(code_data=scan_track).exists()
            if entry_exists:
                context={
                    "error":"Tracking number already exists!"
                }
                return render(request,'delivery/msg_fail.html', context=context)
            else:
                qr_code_scan=QRCodeData(receiver=scan_receiver, code_data=scan_track)
                qr_code_scan.save()
                context={
                    "message":"Data save successfully!"
                }
                return render(request,'delivery/msg_success.html', context=context)
    return render(request,'delivery/add_scan.html')

@login_required
def DaddgenView(request):
    return render(request,'delivery/add_generate2.html')

@login_required
def DmsgSuccessView(request):
    context={"message":"This is default message"}
    return render(request,'delivery/msg_success.html', context=context)

@login_required
def DmsgFailView(request):
    context={"error":"This is default message"}
    return render(request,'delivery/msg_fail.html', context=context)