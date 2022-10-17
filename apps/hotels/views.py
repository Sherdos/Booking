

from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect, render

from apps.hotels.models import Booking, Class, Comments, Hotel, People
from apps.places.models import Places
from apps.settings.models import Currency, Setting

# Create your views here.

def hotel(request, slug):
    setting = Setting.objects.latest('id')
    places = Places.objects.get(slug = slug)
    currency = Currency.objects.all()
    context = {
        'setting':setting,
        'places' :places,
        'currency':currency
    }
    return render(request, 'hotel/hotel.html', context)


def detail_hotel(request, id):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
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
        'currency':currency,
        'hotel_people':hotel_people,
        'hotel_class': hotel_class,
        'commen': commen
    }
    return render(request, 'hotel/detail_hotel.html', context)


def hotel_search(request):
    hotels = Hotel.objects.all()
    setting = Setting.objects.latest('id')
    search_key = request.GET.get('key')
    currency = Currency.objects.all()
    if search_key:
        hotels = Hotel.objects.filter(Q(city__title__icontains   = search_key.title()))
    context = {
        'hotels' : hotels,
        'setting' : setting,
        'currency':currency
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


def booking(request, id):
    setting = Setting.objects.latest('id')
    hotel = Hotel.objects.get(id = id)
    hotel_class = Class.objects.all()
    hotel_people = People.objects.all()
    currency = Currency.objects.all()
    if request.method == 'POST':
        clas = request.POST.get('class')
        people = request.POST.get('people')
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        email = hotel.user.email
        booking = Booking.objects.create(user = request.user,  hotel = hotel, clas_id = clas, people_id = people, date1 = date1, date2 = date2)
        print(booking.clas.clas)
        send_mail(
                    #title:
                    f'Booking',
                    #message:
                    f'Вашем отеле забронировали номер. Требование класс номера {booking.clas.clas} для {booking.people.people}. Заедут в {date1} отедут в {date2}',
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
        'hotel_people':hotel_people,
        'currency':currency
    }
    return render(request, 'hotel/booking.html', context)


def update_hotel(request, id):
    setting = Setting.objects.latest('id')
    currency = Currency.objects.all()
    hotel = Hotel.objects.get(id=id)
    places = Places.objects.all()
    if request.method == 'POST':
        if 'update' in request.POST:
            title = request.POST.get('title')
            description = request.POST.get('desription')
            city = request.POST.get('city')
            currency = request.POST.get('currency')
            price = request.POST.get('price')
            hotel.title = title
            hotel.description = description
            hotel.city_id = city
            hotel.currency_id = currency
            hotel.price = price
            hotel.save()
            return redirect('detail_hotel', hotel.id)
        if 'delete' in request.POST:
            hotel.delete()
            return redirect('detail_hotel', hotel.id)
        if 'hotel_image' in request.POST:
            image = request.FILES.get('image')
            if image:
                hotel.image = image
                hotel.save()
                return redirect('detail_hotel', hotel.id)
            else:
                return redirect('detail_hotel', hotel.id)
    context = {
        'setting':setting,
        'currency': currency,
        'places':places,
        'hotel':hotel
    }
    return render(request, 'hotel/update_hotel.html', context)

