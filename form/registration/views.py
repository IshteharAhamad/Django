from django.shortcuts import render
from .forms import Registration

# Create your views here.


def details(request):
    fm = Registration()
    return render(request, 'demo.html', {'form': fm})
