# Create your models here.
from django.db import models
import uuid


class Transactions(models.Model):
    id =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payer = models.CharField(max_length=20,blank=True)
    receiver = models.CharField(max_length=20,blank=True)
    amount = models.FloatField()
    description = models.TextField(null=True,blank=True)
    company = models.CharField(max_length=20,blank=True)
    project = models.CharField(max_length=20,blank=True)
    status = models.CharField(max_length=20, default='Pending',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active =  models.BooleanField(default=True)
    transaction_date = models.DateField(null=True)
    is_check =  models.BooleanField(default=False)

    def _str_(self):
        return self.id
