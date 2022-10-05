from django.urls import path
from apps.settings.views import about_us, not_setting, place_detail, error_register, not_user

urlpatterns = [
    path('not_setting', not_setting, name='not_setting'),
    path('about_us', about_us, name='about_us' ),
    path('register/error/user', error_register, name='error_register'),
    path('not/user', not_user, name='not_user')
    
]
