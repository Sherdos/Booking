from unicodedata import name
from django.urls import path
from apps.hotels.views import detail_hotel, hotel_search, create_hotel, booking, update_hotel

urlpatterns = [
    path('<int:id>/', detail_hotel, name='detail_hotel'),
    path('hotels/', hotel_search, name='hotel_search'),
    path('create_hotel/', create_hotel, name='create_hotel'),
    path('booking/<int:id>/', booking, name='booking'),
    path('update/<int:id>/', update_hotel, name='update_hotel')
]