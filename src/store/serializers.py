from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    inventory = serializers.IntegerField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)
    last_update = serializers.DateTimeField()