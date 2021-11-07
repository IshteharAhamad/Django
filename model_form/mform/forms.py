from django import forms


class Registration(forms.Form):
    name = forms.CharField(label='User Name', min_length=5, max_length=15)
    email = forms.EmailField(label_suffix=' ', label='Email Id', max_length=25, min_length=5, error_messages={
                             'required': 'fill Email Id here'})
    Password = forms.CharField(widget=forms.PasswordInput())
