from rest_framework import serializers
from .models import *


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ['id','payer','receiver','amount','description','company','project','status','transaction_date']