from django.db import models

# Create your models here.
class Product(models.Model):
    class Meta:
        db_table = "product"
    name = models.CharField(max_length=200)
    eventType = models.CharField(max_length=200)
    price = models.IntegerField()
    imgURL = models.CharField(max_length=200)
    company = models.CharField(max_length=200)

class Event(models.Model):
    class Meta:
        db_table = "event"
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200,default='')
    imgUrl = models.CharField(max_length=200)

class Feature(models.Model):
    class Meta:
        db_table = "feature"
    name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    parcel = models.BooleanField()
    coffee = models.BooleanField()
    fried = models.BooleanField()
    atm = models.BooleanField()
    toto = models.BooleanField()
    hour24 = models.BooleanField()
    loto = models.BooleanField()

    
    