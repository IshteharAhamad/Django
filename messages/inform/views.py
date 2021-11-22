from django.shortcuts import render, HttpResponse
from .models import User
from .forms import Registration
from django.contrib import messages


def message(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            fm.save()

            messages.add_message(request, messages.SUCCESS,
                                 "Data inserted successfully !!!")
            messages.info(request, "Log In successfully")
            fm = Registration()
    else:
        fm = Registration()
    return render(request, 'msg.html', {'form': fm})
