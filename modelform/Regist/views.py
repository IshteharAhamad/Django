from django.shortcuts import render
from .forms import Registration
from .models import User


def details(request):
    p = User.objects.get(pk=2)
    #fm = Registration(request.POST, instance=p)
    if request.method == 'POST':

        fm = Registration(request.POST, instance=p)
        if fm.is_valid():
            """ nm = fm.cleaned_data['name']
             el = fm.cleaned_data['email']
             pwd = fm.cleaned_data['password']
             reg = User(name=nm, email=el, password=pwd)"""
            fm.save()
    else:
        fm = Registration()
    return render(request, 'index.html', {'form': fm})
