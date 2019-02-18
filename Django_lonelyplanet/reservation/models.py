from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from home_site.models import Country,City,Sights,Hotels
import datetime

private_storage = FileSystemStorage(location=settings.STATIC_URL)


# Create your models here.
class car(models.Model):
    use_in_migrations = True
    car_id = models.AutoField(primary_key=True)
    location = models.ForeignKey('home_site.Sights')
    from_date = models.DateField(("Date"))
    from_time = models.TimeField(("Time"))
    to_date = models.DateField(("Date"))
    to_time = models.TimeField(("Time"))


    def __str__(self):
        return self.location

class hotel(models.Model):
    use_in_migrations = True
    hotel_id = models.AutoField(primary_key=True)
    hotels = models.ForeignKey('home_site.Hotels')
    from_date = models.DateField(("Date"))
    to_date = models.DateField(("Date"))
    person_number = models.IntegerField(default="1")


    def __str__(self):
        return self.hotels