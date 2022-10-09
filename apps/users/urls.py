from django.urls import path
from apps.users.views import register, login_user, status_user, user_profile, update

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('<int:id>/', status_user, name='status_user'),
    path('profile/<int:id>/', user_profile, name='user_profile'),
    path('update/profile/<int:id>/', update, name='update_user')
]
