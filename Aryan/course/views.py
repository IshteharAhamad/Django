from django.shortcuts import render

def pythn(request):
    #course={'nm':'django','dn':'4 month','fee':6000}
    student={'name':'Khan',
             'Roll':12,
             'Mob':9879786,
    }
    return render(request,'course/courseone.html',student)
def DJ(request):
    std={
        'std1':{'name':'khan','branch':'cse','roll':12},
        'std2':{'name':'arif','branch':'cse','roll':13},
        'std3':{'name':'jignesh','branch':'IT','roll':14},
        'std4':{'name':'vishal','branch':'IT','roll':15},
    }
    student={'data':std}
    return render(request,'course/coursetwo.html',student)
def Image(request):
    return render(request,'course/co.html',{'nm':'just checking','value':'this is my first page'})
def inner(request):
    return render(request,'course/cor.html',{'nm':"bhai jaan",'value':"wada raha"})
