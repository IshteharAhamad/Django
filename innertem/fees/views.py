from django.shortcuts import render

# Create your views here.
def python(request):
    kn={'nm':"king",
         'last':"khan"
    }
    return render(request,'fees/info.html',kn)