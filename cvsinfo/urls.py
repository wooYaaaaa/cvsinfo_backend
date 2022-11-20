from django.urls import path, include
from .views import getProductInfo, getEventInfo

urlpatterns = [
    path("ProductInfo/", getProductInfo),
    path("EventInfo/", getEventInfo),
]
