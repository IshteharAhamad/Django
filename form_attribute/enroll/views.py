from django.shortcuts import render
from .forms import registration


def showdata(request):
    fm = registration(auto_id=True, label_suffix=' ', initial={
                      'first_name': 'ishtehar ', 'last_name': 'khan', 'email': 'xyz@gmail.com'})
    fm.order_fields(field_order=['email', 'first_name', 'last_name'])
    return render(request, 'hello.html', {'form': fm})
