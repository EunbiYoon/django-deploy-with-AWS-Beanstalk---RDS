from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homeView(request):
    return render(request, 'base/home.html')

@login_required(login_url='login_url')
def securityhomeView(request):
    return render(request, 'base/securityhome.html')

@login_required(login_url='login_url')
def reinventhomeView(request):
    return render(request, 'base/reinventhome.html')