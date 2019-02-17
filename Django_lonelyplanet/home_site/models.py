from django.db import models

class Country(models.Model):

    country_id = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100)
    country_title = models.CharField(max_length=200)
    country_desc = models.CharField(max_length=500)
    country_img = models.ImageField(default="default.jpeg")
    country_rate = models.IntegerField(null=True)

    def __str__(self):
        return self.country_name


class City (models.Model):
    city_id = models.IntegerField(primary_key=True)
    city_name = models.CharField(max_length=100)
    city_title = models.CharField(max_length=200)
    city_desc = models.CharField(max_length=500)
    city_img = models.ImageField(default="default.jpeg")
    city_rate = models.IntegerField(null=True)
    country_id = models.ForeignKey(Country, related_name='count')
	


class Experience(models.Model):
    exp_id= models.AutoField(primary_key=True)
    exp_title=models.CharField(max_length=200,null=False)
    exp_description=models.CharField(max_length=250,null=False)
    exp_img=models.CharField(max_length=200)
    city=models.ForeignKey(City)

class Sights(models.Model):
    sight_id=models.AutoField(primary_key=True)
    sight_name=models.CharField(max_length=200,null=False)
    sight_img=models.CharField(max_length=200)
    city=models.ForeignKey(City)

class Comments(models.Model):
    comment_id=models.AutoField(primary_key=True)
    comment_description=models.CharField(max_length=250)
   # user=models.ForeignKey(Users)
    city=models.ForeignKey(City)
    exp=models.ForeignKey(Experience)





