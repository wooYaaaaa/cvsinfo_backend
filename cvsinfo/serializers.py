from rest_framework import serializers
from .models import Product, Event

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'eventType', 'price', 'imageURL', 'company')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('eventTitle', 'eventSubTitle', 'eventImageURL', 'eventLinkURL', 'eventCompany')
