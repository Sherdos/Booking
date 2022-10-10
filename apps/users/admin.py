
from django.contrib import admin
from apps.users.models import User, Work_us 

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'status_user')
    search_fields = ('username', 'email', 'date_joined', 'status_user')

class Work_usAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')
    search_fields = ('user', 'created')

admin.site.register(User, UserAdmin)
admin.site.register(Work_us, Work_usAdmin)