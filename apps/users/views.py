from multiprocessing import context
from re import T
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect
from apps.settings.models import Setting
from apps.users.models import User

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

def status_user(request, id):
    user = User.objects.get(id=id)
    setting = Setting.objects.latest('id')
    if request.method == 'POST':
        if user.status_user == False:
            user.status_user = True
            user.save()
            return redirect('index')
        else:
            return redirect('index')

    context = {
        'user' :user,
        'setting': setting
    }
    return render(request, 'users/status_user.html', context )


def user_profile(request, id):
    setting = Setting.objects.latest('id')
    user = User.objects.get(id=id)
    context = {
        'setting':setting,
        'user':user
    }
    return render(request, 'user/user_detail.html', context)
