from unicodedata import name
from django.urls import path
from apps.hotels.views import detail_hotel, hotel_search

urlpatterns = [
    path('<int:id>/', detail_hotel, name='detail_hotel'),
    path('hotels/', hotel_search, name='hotel_search')
]