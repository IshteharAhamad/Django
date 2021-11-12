from django.core import validators
from django import forms
from django.forms import fields
from .models import User


class Registration(forms.ModelForm):
    class Meta:
        model = User
        #fields = ['Name', 'Email', 'Password']
        fields = "__all__"
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'Email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': ' Email Id'}),
            'Password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': '* * * * * * *'}),
        }
