
from django.shortcuts import render
from apps.settings.models import Setting
from apps.countries.models import Nation
from apps.settings.models import Currency
from apps.places.models import Places, Places_for_rest
from apps.hotels.models import Hotel
# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    
    currency = Currency.objects.all()
    nation = Nation.objects.all().order_by('?')[:5]
    places = Places_for_rest.objects.all().order_by('?')[:4]
    places_slug = Places.objects.all()
    hotels = Hotel.objects.all()
    
    context = {
        'setting' : setting,
        'places_slug':places_slug,
        'currency' : currency,
        'nation' : nation,
        'places' : places,
        'hotels':hotels
    }
    return render(request, 'index.html', context)

def about_us(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting
    }
    return render(request, 'about-us.html', context)

def place_detail(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting':setting
    }
    return render(request, 'place_detail.html', context)
    
