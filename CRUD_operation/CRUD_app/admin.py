from django.contrib import admin
from .models import User


@admin.register(User)
class Admin_user(admin.ModelAdmin):
    list_display = ['Id', 'Name', 'Email', 'Password']
