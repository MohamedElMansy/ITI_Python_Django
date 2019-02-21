from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
private_storage = FileSystemStorage(location=settings.STATIC_URL)


class Country(models.Model):

    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_title = models.CharField(max_length=200)
    country_desc = models.CharField(max_length=500)
    country_img = models.ImageField(default="default.jpg")
    country_img = models.FileField(storage=private_storage)
    country_rate = models.IntegerField(null=True)

    def __str__(self):
        return self.country_name


class City (models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)
    city_title = models.CharField(max_length=200)
    city_desc = models.CharField(max_length=500)
    city_img = models.ImageField(default="default.jpeg")
    city_img = models.FileField(storage=private_storage)
    city_rate = models.IntegerField(null=True)
    country_id = models.ForeignKey(Country, related_name='count')
    def __str__(self):
        return self.city_name
	


class Experience(models.Model):
    exp_id= models.AutoField(primary_key=True)
    exp_title=models.CharField(max_length=200,null=False)
    exp_description=models.CharField(max_length=250,null=False)
    exp_img=models.ImageField(default="default.jpeg")
    city=models.ForeignKey(City)
    user=models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Sights(models.Model):

    sight_id=models.AutoField(primary_key=True)
    sight_name=models.CharField(max_length=200,null=False)
    sight_img=models.ImageField(default="default.jpeg")
    sight_img = models.FileField(storage=private_storage)
    city=models.ForeignKey(City)

    def __str__(self):
        return self.sight_name

class Comments(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment_description=models.CharField(max_length=250)
    user=models.ForeignKey(User)
    city=models.ForeignKey(City)
    exp=models.ForeignKey(Experience)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Hotels(models.Model):
    hotel_id=models.AutoField(primary_key=True)
    hotel_name=models.CharField(max_length=200,null=False)
    hotel_img=models.ImageField(default="default.jpeg")
    hotel_img = models.FileField(storage=private_storage)
    city=models.ForeignKey(City)

    def __str__(self):
        return self.hotel_name



