from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Event, Feature
from .serializers import ProductSerializer, EventSerializer, FeatureSerializer

# Create your views here.
@api_view(['GET'])
def getProductInfo(request):
    ProductInfo = list(Product.objects.all())
    serializerProduct = ProductSerializer(ProductInfo, many=True)
    return Response(serializerProduct.data)

@api_view(['GET'])
def getEventInfo(request):
    EventInfo = list(Event.objects.all())
    serializerEvent = EventSerializer(EventInfo, many=True)
    return Response(serializerEvent.data)

@api_view(['GET'])
def getFeatureInfo(request):
    FeatureInfo = list(Feature.objects.all())
    serializerFeature = FeatureSerializer(FeatureInfo, many=True)
    return Response(serializerFeature.data)
