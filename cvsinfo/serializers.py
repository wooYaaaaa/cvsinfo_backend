from rest_framework import serializers
from .models import Product, Event, Feature

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'eventType', 'price', 'imgURL', 'company')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'company', 'imgUrl')

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('name', 'company', 'parcel', 'coffee', 'fried', 'atm', 'toto', 'hour24', 'loto')