from django.urls import path
from apps.places.views import hotel

urlpatterns = [
    path('hotel/<str:slug>/', hotel, name='hotel'),

]
