from django.shortcuts import render
from django.http import HttpResponse
def services(request):
    return HttpResponse('<center><h1>There are many services here...</h1></center>')

def king(request):
    return HttpResponse("helllooo...")
