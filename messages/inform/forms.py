from django import forms
from django.db.models import fields
from inform.models import User
from django.core import validators


class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Id '}),
            'password': forms.PasswordInput(render_value=True, attrs={'class': 'form-control', 'placeholder': '* * * * * * * *'})
        }
