from django.shortcuts import render

def Pf(request):
    return render(request,'fees/fee.html',{'nm':'king','value':'first page'})
def Df(request):
    return render(request,'fees/fee1.html')
def join(request):
    return render(request,'fees/fees.html',{'nm':'kuch bhi','value':'something'})