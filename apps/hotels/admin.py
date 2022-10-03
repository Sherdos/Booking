from django.contrib import admin
from apps.hotels.models import Hotel, Class, People, Booking, Comments

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Class)
admin.site.register(People)
admin.site.register(Booking)
admin.site.register(Comments)