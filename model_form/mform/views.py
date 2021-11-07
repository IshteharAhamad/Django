from django.shortcuts import render
from .forms import Registration
from .models import Users
from django.views.decorators.csrf import csrf_protect


def showdetails(request):
    fm = Registration(request.POST)
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nam = fm.cleaned_data['name']
            emai = fm.cleaned_data['email']
            pwd = fm.cleaned_data['Password']
            reg = Users(Id=6, User_name=nam, Email_Id=emai, Password=pwd)
           # reg.save()
            reg.delete()

    return render(request, 'index.html', {'form': fm})
