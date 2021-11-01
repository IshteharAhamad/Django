from django.shortcuts import render
from django.http import HttpRequest
def Fees(request):
   return render(request,'fees.html')
def Fees1(request):
   return render(request,'feespy.html')


