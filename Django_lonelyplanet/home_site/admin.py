from django.contrib import admin
from .models import Country ,City,Sights,Hotels
# Register your models here.

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Sights)
admin.site.register(Hotels)