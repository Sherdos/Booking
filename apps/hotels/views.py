
from django.db.models import Q
from django.shortcuts import render, redirect
from apps.settings.models import Currency, Setting
from apps.places.models import Places
from apps.hotels.models import Booking, Hotel, People, Class, Comments
from django.core.mail import send_mail
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
    hotel_class = Class.objects.all()
    hotel_people = People.objects.all()
    commen = Comments.objects.filter(hotel = hotels)
    if request.method == 'POST':
        if 'comments' in request.POST:
            comment = request.POST.get('comment')
            comments = Comments.objects.create(user = request.user, hotel = hotels, comment = comment)
            return redirect('detail_hotel', hotels.id)
    context = {
        'setting':setting,
        'hotels':hotels,
        'hotel':hotel,
        'hotel_people':hotel_people,
        'hotel_class': hotel_class,
        'commen': commen
    }
    return render(request, 'hotel/detail_hotel.html', context)


def hotel_search(request):
    hotels = Hotel.objects.all()
    setting = Setting.objects.latest('id')
    search_key = request.GET.get('key')
    if search_key:
        hotels = Hotel.objects.filter(Q(city__title__icontains   = search_key.title()))
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
        if 'booking' in request.POST:
            image = request.FILES.get('image')
            title = request.POST.get('title')
            description = request.POST.get('description')
            city = request.POST.get('city')
            price = request.POST.get('price')
            currency = request.POST.get('currency')
            hotel = Hotel.objects.create(user = request.user, title = title, description = description, city_id = city, image = image, price = price, currency_id = currency)
            return redirect('index')
        if 'comment' in request.POST:
            comment = request.POST.get('comment')
            comments = Comments
    context = {
        'setting' : setting,
        'currency':currency,
        'places':places
     }
    return render(request, 'hotel/create_hotel.html', context)

def booking(request, id):
    setting = Setting.objects.all()
    hotel = Hotel.objects.get(id = id)
    hotel_class = Class.objects.all()
    hotel_people = People.objects.all()
    if request.method == 'POST':
        clas = request.POST.get('class')
        people = request.POST.get('people')
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        email = hotel.user.email
        
        booking = Booking.objects.create(user = request.user,  hotel = hotel, clas_id = clas, people_id = people, date1 = date1, date2 = date2)
        send_mail(
                    #title:
                    f'Booking',
                    #message:
                    f'Вашем отеле забронировали номер. Требование класс номера {clas} для {people}. Заедут в {date1} отедут в {date2}',
                    #from:
                    'noreply@somehost.local',
                    #to:
                    [email]

        )
        return redirect('index')
    

    context = {
        'setting':setting,
        'hotel' : hotel,
        'hotel_class':hotel_class,
        'hotel_people':hotel_people
    }

    return render(request, 'hotel/booking.html', context)



