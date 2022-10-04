
from django.shortcuts import redirect, render
from apps.settings.models import Setting
from apps.countries.models import Nation
from apps.settings.models import Currency
from apps.places.models import Places, Places_for_rest
from apps.hotels.models import Hotel, Comments
# Create your views here.
def index(request):
    try:

        setting = Setting.objects.latest('id')
    except:
        return redirect('not_setting')
    comments = Comments.objects.all().order_by('?')[:3]
    currency = Currency.objects.all()
    nation = Nation.objects.all().order_by('?')[:5]
    places = Places_for_rest.objects.all().order_by('?')[:4]
    places_slug = Places.objects.all()
    hotels = Hotel.objects.all().order_by('?')[:3]
    
    context = {
        'setting' : setting,
        'places_slug':places_slug,
        'currency' : currency,
        'nation' : nation,
        'places' : places,
        'hotels':hotels,
        'comments':comments
    }
    return render(request, 'index.html', context)

def about_us(request):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    context = {
        'setting' : setting,
        'currency': currency
    }
    return render(request, 'about-us.html', context)

def place_detail(request):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    context = {
        'setting':setting,
        'curroncy':currency
    }
    return render(request, 'place_detail.html', context)

def not_setting(request):
    return render(request, 'settings/not_setting.html')
    
