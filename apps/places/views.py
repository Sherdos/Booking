from django.shortcuts import render
from apps.hotels.models import Hotel
from apps.settings.models import Setting
from apps.places.models import Places_for_rest, Places

# Create your views here.

def hotel(request, slug):
    setting = Setting.objects.latest('id')
    places = Places.objects.get(slug = slug)

    context = {
        'setting':setting,
        'places' :places,

    }
    return render(request, 'hotel/hotel.html', context)

def popular(request):
    setting = Setting.objects.latest('id')
    places = Places_for_rest.objects.all()

    context = {
        'setting':setting,
        'places' :places,

    }
    return render(request, 'popular.html', context)
