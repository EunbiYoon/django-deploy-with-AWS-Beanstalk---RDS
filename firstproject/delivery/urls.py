from django.urls import path
from .views import DhomeView, DsearchView, DsearchcheckoutView, DcheckoutView, DaddscanView, DaddView, DaddgenView, DmsgSuccessView, DmsgFailView

urlpatterns = [
    path('',DhomeView,name='Dhome_url'),
    path('search',DsearchView, name='Dsearch_url'),
    path('search/checkout',DsearchcheckoutView, name='Dsearchout_url'),
    path('checkout',DcheckoutView,name="Ddeliverycheckout_url"),
    path('add',DaddView,name='Dadd_url'),
    path('add/generate',DaddgenView,name='Daddgen_url'),
    path('add/scan',DaddscanView,name='Daddscan_url'),
    path('success',DmsgSuccessView,name='Dmsgsuccess_url'),
    path('error',DmsgFailView,name='Dmsgfail_url')
]