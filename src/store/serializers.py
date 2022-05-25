from dataclasses import fields
from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'inventory', 'unit_price', 'last_update']
    
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, source='price')
    