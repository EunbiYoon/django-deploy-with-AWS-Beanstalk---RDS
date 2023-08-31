from django.urls import path
from .views import PhomeView, PviolatorView, PviolatorlistView, PviolatordeleteView, PemployeeView, PemployeelistView

urlpatterns = [
    path('',PhomeView,name='Phome_url'),
    path('violator/register',PviolatorView,name='Pviolator_url'),
    path('violator/list',PviolatorlistView,name='Pviolator_list_url'),
    path('violator/delete/<int:data_id>',PviolatordeleteView,name='Pviolator_delete_url'),
    path('employee_of_month/register',PemployeeView,name='Pemployee_url'),
    path('employee_of_month/list',PemployeelistView,name='Pemployee_list_url')
]