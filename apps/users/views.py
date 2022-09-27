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
            user = User.objects.create(email = email, username = username)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return redirect('register')
    context = {
        'setting' : setting
        }
    return render(request, 'users/register.html', context )

def login_user(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username=username, password = password)
        login(request, user)
        return redirect('index')
    context = {
        "setting" : setting
    
    }
    return render(request, 'users/login.html', context)

