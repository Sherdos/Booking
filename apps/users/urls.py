from django.urls import path
from apps.users.views import register, login_user, status_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('<int:id>/', status_user, name='status_user')
]
