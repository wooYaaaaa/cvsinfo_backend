from rest_framework import serializers
from .models import Product, Event

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'eventType', 'price', 'imgURL', 'company')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'company', 'imgUrl')
