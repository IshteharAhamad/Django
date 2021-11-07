from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import aryan


def success(request):
    return render(request, 'demo.html')


def detail(request):
    fm = aryan()
    if request.method == 'POST':
        fm = aryan(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['first_name']
            last = fm.cleaned_data['last_name']
            email = fm.cleaned_data['email']
            print('First Name :', name)
            print('last Name :', last)
            print('email :', email)
            return HttpResponseRedirect('/student/success/')
           # return render(request, 'demo.html', {'nm': name, 'ls': last, 'email': email})
    return render(request, 'khan.html', {'form': fm})
