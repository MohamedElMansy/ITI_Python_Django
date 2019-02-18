from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CarForm
from .models import car
from home_site.models import Country,City,Sights


def newcar(request,city_id):
    car_form = CarForm()
    car_form.fields['location'].queryset = Sights.objects.filter(city_id = city_id)
    car_form.fields['location'].empty_label = "Select your location"
    if request.method == "POST":
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_form.save()
            return HttpResponseRedirect(request.path_info)

    context = {"form": car_form}
    return render(request, "car/car_form.html", context)