from django.db import models

class Country(models.Model):

    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_title = models.CharField(max_length=200)
    country_desc = models.CharField(max_length=500)
    country_img = models.ImageField(default="default.jpeg")
    country_rate = models.IntegerField(null=True)

class City (models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)
    city_title = models.CharField(max_length=200)
    city_desc = models.CharField(max_length=500)
    city_img = models.ImageField(default="default.jpeg")
    city_rate = models.IntegerField(null=True)
    country_id = models.ForeignKey(Country)




