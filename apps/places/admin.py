from django.contrib import admin
from apps.places.models import Places, Places_for_rest
# Register your models here.
class PlacesAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug' : ('title', )}
admin.site.register(Places,PlacesAdmin)
admin.site.register(Places_for_rest)