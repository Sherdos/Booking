from django.shortcuts import render
from apps.settings.models import Setting, Currency
from apps.places.models import Places_for_rest, Places

# Create your views here.

def popular(request):
    setting = Setting.objects.latest('id')
    places = Places_for_rest.objects.all()
    currency = Currency.objects.all()
    context = {
        'setting':setting,
        'places' :places,
        'currency':currency
    }
    return render(request, 'popular.html', context)
