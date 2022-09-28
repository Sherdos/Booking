from django.urls import path
from apps.places.views import hotel, popular

urlpatterns = [
    path('hotel/<str:slug>/', hotel, name='hotel'),
    path('popular/', popular, name='popular')

]
