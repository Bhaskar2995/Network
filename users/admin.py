from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,UserInfo 
from users.models import Restaurant, Person

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
admin.site.register(UserInfo)
admin.site.register(Restaurant)
admin.site.register(Person)
# Register your models here.
