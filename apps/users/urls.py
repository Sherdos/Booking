from django.contrib.auth import views as auth_views
from django.urls import path

from apps.users.views import (forget, login_user, register, status_user,
                              update, user_profile)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('<int:id>/', status_user, name='status_user'),
    path('profile/<int:id>/', user_profile, name='user_profile'),
    path('update/profile/<int:id>/', update, name='update_user'),
    path('forget/', forget, name='forget'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="users/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'), 
]
