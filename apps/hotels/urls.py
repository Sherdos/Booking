from unicodedata import name
from django.urls import path
from apps.hotels.views import detail_hotel, hotel_search, create_hotel

urlpatterns = [
    path('<int:id>/', detail_hotel, name='detail_hotel'),
    path('hotels/', hotel_search, name='hotel_search'),
    path('create_hotel/', create_hotel, name='create_hotel')
]