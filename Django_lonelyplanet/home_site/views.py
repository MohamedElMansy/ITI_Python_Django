from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Country,City,Experience,Comments,Sights,User

# Create your views here.
def index(request):
    all_countris=Country.objects.all().order_by('country_rate')[:6]
    context = {'countries': all_countris}
    return render(request, 'index.html', context)

def show_city(request,city_id):
    all_countris = Country.objects.all().order_by('country_rate')[:6]
    single_city=City.objects.get(city_id = city_id)
    sight = Sights.objects.filter(city_id=city_id)
    all_exp = Experience.objects.filter(city_id=city_id).select_related('user')
    all_comments=Comments.objects.filter(city_id=city_id).select_related('user').select_related('exp')
    context = {'city': single_city,'sights':sight,'countries': all_countris ,'exps':all_exp,'comms':all_comments}
    add_comment(request)
    return render(request, 'single_city.html', context)

def add_comment(request):
    if request.method=='POST':
        if request.POST.get('exp') and request.POST.get('comment') \
                and request.POST.get('city') and request.POST.get('id'):
            comm = Comments()
            comm.comment_description = request.POST.get('comment')
            comm.user_id = request.POST.get('id')
            comm.city_id = request.POST.get('city')
            comm.exp_id = request.POST.get('exp')
            comm.save()





def country_render(request, ct_id):
    country_id = Country.objects.get(country_id=eval(ct_id))
    cities = City.objects.filter(country_id_id=eval(ct_id))
    countries= Country.objects.all()
    context = {'city': cities, 'ct': country_id,'count':countries}
    return render(request, "country.html", context)

