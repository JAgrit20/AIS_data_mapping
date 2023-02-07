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

