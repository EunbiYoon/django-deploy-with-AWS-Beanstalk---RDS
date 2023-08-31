from django.db import models
from user.models import CustomUser

# Create your models here.
class IdData(models.Model):
    visitor_name=models.CharField(max_length=255, null=False, blank=False)
    visitor_company=models.CharField(max_length=255, null=False, blank=False)
    start_date=models.DateTimeField(null=False, blank=False)
    end_date=models.DateTimeField(null=False, blank=False)
    visitor_purpose=models.TextField(null=False, blank=False)
    bring_laptop=models.CharField(max_length=255, null=False, blank=False)
    pic=models.CharField(max_length=255, null=False, blank=False)
    register_at=models.DateTimeField(auto_now_add=True)
    remark=models.TextField(null=True, blank=True)
    show_remark=models.BooleanField(default=False)
    reject_request=models.BooleanField(default=False)
    #checkout
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    security_approval=models.DateTimeField(null=True, blank=True)
    check_in=models.DateTimeField(null=True, blank=True)
    check_out=models.DateTimeField(null=True, blank=True)
