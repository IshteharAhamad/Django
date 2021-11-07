from django.contrib import admin
from .models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('Id', 'User_name', 'Email_Id', 'Password')
