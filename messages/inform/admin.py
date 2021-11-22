from django.contrib import admin
from .models import User


@admin.register(User)
class admin_user(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
