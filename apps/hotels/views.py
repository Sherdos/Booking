from django.db.models import Q
from django.shortcuts import render, redirect
from apps.settings.models import Currency, Setting
from apps.places.models import Places
from apps.hotels.models import Hotel
# Create your views here.
# def hotel_search(request, slug):
#     setting = Setting.objects.latest('id')
#     places = Places.objects.get(slug = slug)
#     if request.method == 'POST':
#         if 'hotel_detail' in request.POST:
#             slug = request.POST.get(slug)
#             return redirect('hotel',places.slug)
#     context = {
#         'setting' : setting,
#         'places' : places
#     }
#     return render(request, 'index.html', context)



def detail_hotel(request, id):
    setting = Setting.objects.latest('id')
    hotels = Hotel.objects.get(id=id)
    hotel = Hotel.objects.all()
    context = {
        'setting':setting,
        'hotels':hotels,
        'hotel':hotel
    }
    return render(request, 'hotel/detail_hotel.html', context)


def hotel_search(request):
    hotels = Hotel.objects.all()
    setting = Setting.objects.latest('id')
    search_key = request.GET.get('key')
    if search_key:
        hotels = Hotel.objects.filter(Q(city__title__icontains = search_key))
    context = {
        'hotels' : hotels,
        'setting' : setting,
    }
    return render(request, 'hotel/search_hotels.html', context)

def create_hotel(request):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    places = Places.objects.all()
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        city = request.POST.get('city')
        price = request.POST.get('price')
        currency = request.POST.get('currency')
        hotel = Hotel.objects.create(user = request.user, title = title, description = description, city_id = city, image = image, price = price, currency_id = currency)
        return redirect('index')
    context = {
        'setting' : setting,
        'currency':currency,
        'places':places
     }
    return render(request, 'hotel/create_hotel.html', context)
