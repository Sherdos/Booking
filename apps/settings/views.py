from datetime import datetime
from django.shortcuts import redirect, render
from apps.settings.models import Setting
from apps.countries.models import Nation
from apps.settings.models import Currency
from apps.places.models import Places, Places_for_rest
from apps.hotels.models import Hotel, Comments
from apps.users.models import User, Work_us
import pytz


# Create your views here.
def index(request):
    try:

        setting = Setting.objects.latest('id')
    except:
        return redirect('not_setting')
    comments = Comments.objects.all().order_by('?')[:3]
    try:
        user = User.objects.get(username=request.user.username)
    except:
        print('error')
    currency = Currency.objects.all()
    nation = Nation.objects.all().order_by('?')[:5]
    places = Places_for_rest.objects.all().order_by('?')[:4]
    places_slug = Places.objects.all()
    hotels = Hotel.objects.all().order_by('?')[:3]
    tz_kg = pytz.timezone("Asia/Bishkek")
    
    try:
        work_us = Work_us.objects.get(user = user)
        now = datetime.now()
        timezone_1 = tz_kg.localize(now)
        
        if timezone_1 >= work_us.created:
            user.status_user = False
            user.save()
            print(f'{user.status_user}')
            work_us.delete()
    except:
    
        print('error')
    
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

def error_register(request):
    return render(request, 'settings/error_register.html')

def not_user(request):
    return render(request, 'settings/not_user.html')

def no_money(request):
    return render(request, 'settings/no_money.html')
