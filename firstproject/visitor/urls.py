from django.urls import path
from .views import VhomeView, VregisterView, VmyView, VlistView, VmydeleteView, VlistdeleteView, VtogglemyView, VtogglelistView, VapprovalView, VpassView, VcheckinView, VcheckoutView

urlpatterns = [
    path('',VhomeView,name='Vhome_url'),
    path('register',VregisterView,name='Vregister_url'),
    path('myapproval',VmyView,name='Vmyapproval_url'),
    path('list',VlistView,name='Vlist_url'),
    path('myapproval/delete/<int:data_id>',VmydeleteView,name='Vmydelete_url'),
    path('list/delete/<int:data_id>',VlistdeleteView,name='Vlistdelete_url'),
    path('myapproval/<int:data_id>', VtogglemyView, name='Vmytoggle_url'),
    path('list/<int:data_id>', VtogglelistView, name='Vlisttoggle_url'),
    path('list/approve/<int:data_id>',VapprovalView, name='Vlistapproval_url'),
    path('list/parkingpass/<int:data_id>', VpassView, name='Vparkingpass_url'),
    path('list/checkin/<int:data_id>', VcheckinView, name='Vcheckin_url'),
    path('list/checkout/<int:data_id>', VcheckoutView, name='Vcheckout_url'),
]