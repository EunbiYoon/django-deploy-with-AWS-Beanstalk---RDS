from django.db import models
from user.models import CustomUser

# Create your models here.
class ReinventData(models.Model):
    program=models.CharField(max_length=100, null=False, blank=False)
    late_day=models.CharField(max_length=100, null=True, blank=True)
    applied_day=models.CharField(max_length=100, null=False, blank=False)
    remark=models.TextField(null=True, blank=True, max_length=76)
    user=models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    request_at=models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.email_teamM()
    
 




