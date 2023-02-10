from django.db import models

# Create your models here.

class AIS_data_past(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    Company_name = models.CharField(max_length=111)
    Speciality_goods = models.CharField(max_length=110)
    Rating = models.FloatField()
    Number_of_ships = models.BigIntegerField()
    Countries = models.TextField()
class AIS_data_routes(models.Model):
    id = models.CharField(max_length=111,primary_key=True)
    Ship_id = models.CharField(max_length=111)
    Latitude = models.CharField(max_length=111)
    Logitude = models.CharField(max_length=111)
class AIS_data_report(models.Model):
    id = models.CharField(max_length=111,primary_key=True)
    RANK = models.CharField(max_length=111)
    SHIPPING_COMPANY = models.CharField(max_length=111)
    Num_of_ships = models.CharField(max_length=111)
    CAPACITY = models.CharField(max_length=111)
    URL     = models.TextField(blank=True, null = True)
class AIS_data_updates(models.Model):
    id = models.CharField(max_length=111,primary_key=True)
    mmsi = models.CharField(max_length=111,blank=True, null = True)
    heading = models.CharField(max_length=111,blank=True, null = True)
    shiptype = models.CharField(max_length=111,blank=True, null = True)
    width = models.CharField(max_length=111,blank=True, null = True)
    length     = models.CharField(max_length=111,blank=True, null = True)


