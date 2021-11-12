from django import forms
from django.db.models import fields
from django.core import validators
from django.forms.widgets import Widget
#from django.forms.models import ErrorMessages
from .models import User


class Registration(forms.ModelForm):
    name = forms.CharField(min_length=5, max_length=12,
                           label_suffix=' ', label='User Name')

    class Meta:
        model = User
        fields = ('Id', 'name', 'email', 'password')
        labels = {'name': ' User Name ',
                  'email': 'Email ID', 'password': 'Password '}
        error_message = {'name': {'required': 'please enter your name'}}
        widgets = {'password': forms.PasswordInput(attrs={'class': 'pwd', 'placeholder': "********"}),
                   'name': forms.TextInput(attrs={'class': 'myclass', 'placeholder': 'Enter your Name Here..'}

                                           )
                   }
