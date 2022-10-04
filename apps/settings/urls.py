from django.urls import path
from apps.settings.views import about_us, not_setting, place_detail

urlpatterns = [
    path('not_setting', not_setting, name='not_setting'),
    path('about_us', about_us, name='about_us' ),
    
]
