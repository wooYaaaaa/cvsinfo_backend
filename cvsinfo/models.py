from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    eventType = models.CharField(max_length=200)
    price = models.IntegerField()
    imageURL = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class Event(models.Model):
    eventTitle = models.CharField(max_length=200)
    eventSubtitle = models.CharField(max_length=200)
    eventImageURL = models.CharField(max_length=200)
    eventLinkURL = models.CharField(max_length=200,default='')
    eventCompany = models.CharField(max_length=200,default='')