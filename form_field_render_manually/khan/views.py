from django.shortcuts import render
from .forms import Registration


def showdetails(request):
    fm = Registration()
    return render(request, 'demo.html', {'form': fm})
