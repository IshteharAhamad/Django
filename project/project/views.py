from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    return render(request,"index.html")
def About_Us(request):
    return HttpResponse("hello ishtehar khan")
def course(request):
    return HttpResponse("<b font-size=16px>Welcome to here you about the course detail:</b>")
def course_detail(request,course_id):
    return HttpResponse(course_id)
