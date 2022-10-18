from datetime import datetime, timedelta
from locale import currency

from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.hotels.models import Hotel
from apps.settings.models import Currency, Setting
from apps.users.models import User, Work_us


# Create your views here.
def register(request):
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            if username and email and password and confirm_password:
                try:
                    user = User.objects.create(email = email, username = username)
                    user.set_password(password)
                    user.save()
                    user = User.objects.get(username = username)
                    user = authenticate(username = username, password=password)
                    login(request, user)
                    return redirect('index')
                except:
                    return redirect('error_register')
            else:
                return redirect('error_register')
        else:
            return redirect('error_register')
    context = {
        'setting' : setting
        }
    return render(request, 'users/register.html', context )

def login_user(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            user = authenticate(username=username, password = password)
            login(request, user)
            return redirect('index')
        except:
            return redirect('not_user')
    context = {
        "setting" : setting
    }
    return render(request, 'users/login.html', context)

def forget(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            check_email = User.objects.get(email = email)
            print(check_email)
            send_mail(
                    # title:
                    f"Восстановить пароль",
                    # message:
                    f"Привет {check_email.username}! Мы получили запрос на сброс пароля для учетной записи Booking, связанной с {email}. Перейдите по ссылке чтобы восстановить доступ к аккаунту https://booking26.herokuapp.com/users/reset/{urlsafe_base64_encode(force_bytes(check_email.pk))}/{default_token_generator.make_token(check_email)}",
                    # from:
                    "noreply@somehost.local",
                    # to:
                    [email]
            )
        except:
            return redirect('forget')
    context = {
        'setting' : setting
    }
    return render(request, 'users/forget.html', context)
        
    

def status_user(request, id):
    user = User.objects.get(id=id)
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        if user.status_user == False:
            try:
                user.balans -= 500
                user.status_user = True
                user.save()
                now = datetime.now()
                end_work = timedelta(30)
                end = now + end_work
                work_us = Work_us.objects.create(user = request.user, created = end)
                return redirect('index')
            except:
                return redirect('no_money')
    context = {
        'user' :user,
        'setting': setting
    }
    return render(request, 'users/status_user.html', context )

def user_profile(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id=id)
    hotel = Hotel.objects.all()
    currency = Currency.objects.all()
    context = {
        'setting':setting,
        'user':user,
        'hotel':hotel,
        'currency':currency
    }
    return render(request, 'users/user_detail.html', context)

def update(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id=id)
    if request.method == 'POST':
        if 'update' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.phone = phone
            user.save()
            return redirect('user_profile', user.id)  
        if 'update_image' in request.POST:
            image = request.FILES.get('image')
            user.profile_image = image
            user.save()
            return redirect('user_profile', user.id)
        if 'delete' in request.POST:
            user.delete()
            return redirect('index')
    context = {
        'setting':setting,
        'user':user
    }
    return render(request, 'users/update.html', context)
