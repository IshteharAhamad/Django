from django import forms


class aryan(forms.Form):
    first_name = forms.CharField(
        label='User Name', label_suffix='  ', initial='aryan khan', required=False)
    last_name = forms.CharField()
    email = forms.EmailField()
    #mobile = forms.CharField(widget=forms.FileInput())
    #Key = forms.CharField(widget=forms.HiddenInput())
