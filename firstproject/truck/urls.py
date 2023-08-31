from django.urls import path
from .views import ThomeView, TcheckinView, TcheckoutView, ThistoryView

urlpatterns = [
    path('',ThomeView,name='Thome_url'),
    path('in',TcheckinView,name='Ttruckin_url'),
    path('out',TcheckoutView,name='Ttruckout_url'),
    path('history',ThistoryView,name='Ttruckhistory_url')
]