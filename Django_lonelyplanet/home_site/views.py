from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Country,City,Experience,Comments,Sights

# Create your views here.
def index(request):
    all_countris=Country.objects.all().order_by('country_rate')[:6]
    context = {'countries': all_countris}
    return render(request, 'index.html', context)

def show_city(request,city_id):
    all_countris = Country.objects.all().order_by('country_rate')[:6]
    single_city=City.objects.get(city_id = city_id)
    sight = Sights.objects.filter(city_id=city_id)
    context = {'city': single_city,'sights':sight,'countries': all_countris}
    return render(request, 'single_city.html', context)

