from django.shortcuts import render
from enroll.models import Student
from .forms import Registration


def display(request):
    std = Student.objects.all()
    return render(request, 'index.html', {'st': std})


def details(request):
    fm = Registration(auto_id=True, label_suffix='   ',
                      initial={'enter': 'name here!'})
    return render(request, 'demo.html', {'form': fm})
