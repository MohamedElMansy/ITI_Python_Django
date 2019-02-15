from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render
from .models import Country,City,Experience,Comments

# Create your views here.
def index(request):
    all_countris=Country.objects.all().order_by('country_rate')[:6]
    context = {'countries': all_countris}
    return render(request, 'index.html', context)
