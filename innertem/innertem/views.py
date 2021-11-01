from django.shortcuts import render
def homepage(request):
    return render(request,'home.html',{'nm':"my home page.."})