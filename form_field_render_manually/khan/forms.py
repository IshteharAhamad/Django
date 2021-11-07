from django import forms


class Registration(forms.Form):
    first_name = forms.CharField(
        initial="aryan khan", help_text="only 20 characters are allowed")
   # last_name = forms.CharField()
   # email = forms.EmailField()
