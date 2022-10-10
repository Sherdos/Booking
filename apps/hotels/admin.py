from django.contrib import admin
from apps.hotels.models import Hotel, Class, People, Booking, Comments

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'currency', 'price', 'city')
    search_fields = ('user', 'title', 'currency', 'price', 'city')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'clas', 'people', 'hotel', 'date1', 'date2')
    search_fields = ('user', 'clas', 'people', 'hotel', 'date1', 'date2')

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Class)
admin.site.register(People)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Comments)