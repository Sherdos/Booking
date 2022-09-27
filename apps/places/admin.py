from django.contrib import admin
from apps.places.models import Places, Places_for_rest
# Register your models here.
admin.site.register(Places)
admin.site.register(Places_for_rest)