from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

# Register your models here.
