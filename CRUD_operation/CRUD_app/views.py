from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import Registration
from django.core import validators

# Add data function


def add_show(request):
    if request.method == "POST":
        fmt = Registration(request.POST)
        if fmt.is_valid():
            nm = fmt.cleaned_data['Name']
            el = fmt.cleaned_data['Email']
            pwd = fmt.cleaned_data['Password']
            reg = User(Name=nm, Email=el, Password=pwd)
            reg.save()
            fmt = Registration()
    else:
        fmt = Registration()
    std = User.objects.all()
    return render(request, 'adddata.html', {'form': fmt, 'show': std})
# Update Data function


def update(request, Id):
    if request.method == 'POST':
        pi = User.objects.get(pk=Id)
        fmt = Registration(request.POST, instance=pi)
        if fmt.is_valid():
            fmt.save()
    else:
        pi = User.objects.get(pk=Id)
        fmt = Registration(instance=pi)
    return render(request, 'update.html', {'form': fmt})
# delete function...


def delete_data(request, Id):
    if request.method == "POST":
        pi = User.objects.get(pk=Id)
        pi.delete()
    return HttpResponseRedirect('/')
