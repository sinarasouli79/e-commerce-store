from dataclasses import fields
from rest_framework import serializers
from .models import Product, Reviews


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description',
                  'inventory', 'unit_price', 'last_update', 'collection']

    unit_price = serializers.DecimalField(
        max_digits=6, decimal_places=2, source='price')


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ['id', 'date', 'name', 'description', 'product',]
        