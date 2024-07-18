from rest_framework import serializers
from .models import Service, Price, Addon

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['vehicle_type', 'amount']

class AddonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addon
        fields = ['name', 'price']

class ServiceSerializer(serializers.ModelSerializer):
    prices = PriceSerializer(many=True)
    addons = AddonSerializer(many=True, required=False)

    class Meta:
        model = Service
        fields = ['id', 'name', 'includes', 'prices', 'addons']