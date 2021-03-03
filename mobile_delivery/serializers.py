from .models import ClearOrders
from rest_framework import serializers


class DeliverySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClearOrders
        fields = ['Order_no','Name','Phone','Shipping_method','Shipping_code','Date_placed','Status','Name_other','Phone_no','Relationship',]
  