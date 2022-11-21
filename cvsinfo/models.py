from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "product"
    name = models.CharField(max_length=200)
    eventType = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    imageURL = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class Event(models.Model):
    class Meta:
        db_table = "event"
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200,default='')
    imgUrl = models.CharField(max_length=200)
    