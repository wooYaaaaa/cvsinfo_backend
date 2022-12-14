from django.urls import path, include
from .views import getProductInfo, getEventInfo, getFeatureInfo

urlpatterns = [
    path("ProductInfo/", getProductInfo),
    path("EventInfo/", getEventInfo),
    path("FeatureInfo/", getFeatureInfo),
]
