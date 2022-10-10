from django.urls import path
from apps.places.views import popular

urlpatterns = [
    path('popular/', popular, name='popular')
]
