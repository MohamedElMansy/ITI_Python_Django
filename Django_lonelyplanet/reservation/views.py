from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import CarForm,HotelForm
from .models import car,hotel,User
from django.contrib.auth.models import User
from home_site.models import Country,City,Sights,Hotels



def newcar(request,city_id):
    car_form = CarForm()
    car_form.fields['location'].queryset = Sights.objects.filter(city_id = city_id)
    car_form.fields['location'].empty_label = "Select your location"
    car_form.fields['destination'].queryset = Sights.objects.filter(city_id = city_id)
    car_form.fields['destination'].empty_label = "Select your destination"
    if request.method == "POST":
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car_reserv = car_form.save(commit=False)
            user_id = request.user.id
            user_instance = User.objects.get(id=user_id)
            car_reserv.user = user_instance
            city_instance = City.objects.get(city_id=city_id)
            car_reserv.city = city_instance
            country_id = City.objects.values('country_id_id').filter(city_id=city_id)
            country_instance = Country.objects.get(country_id=country_id)
            car_reserv.country = country_instance
            car_reserv.save()
            return HttpResponseRedirect(request.path_info)

    context = {"form": car_form}
    return render(request, "car/car_form.html", context)


def newhotel(request,city_id):
    hotel_form = HotelForm()
    user = request.user
    hotel_form.fields['hotels'].queryset = Hotels.objects.filter(city_id = city_id)
    hotel_form.fields['hotels'].empty_label = "Select your hotel"
    hotel_form.fields['person_number'].empty_label = "Number of persons"
    if request.method == "POST":
        hotel_form = HotelForm(request.POST)
        if hotel_form.is_valid():
                reserv = hotel_form.save(commit=False)
                user_id = request.user.id
                user_instance = User.objects.get(id=user_id)
                reserv.user = user_instance
                city_instance = City.objects.get(city_id=city_id)
                reserv.city = city_instance
                country_id = City.objects.values('country_id_id').filter(city_id=city_id)
                country_instance = Country.objects.get(country_id=country_id)
                reserv.country = country_instance
                reserv.save()
                return HttpResponseRedirect(request.path_info)
    context = {"form": hotel_form}
    return render(request, "hotel/hotel_res.html", context)