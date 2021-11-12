from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def show_details(request, my_id):
    if my_id == 1:
        student = {'id': my_id, 'name': 'ishtehar khan'}
    if my_id == 2:
        student = {'id': my_id, 'name': 'aryan khan'}
    if my_id == 3:
        student = {'id': my_id, 'name': 'jignesh Yadav'}
    return render(request, 'show.html', student)


def show_detail(request, my_id, sub):
    if my_id == 1 and sub == 'khan':
        student = {'id': my_id, 'name': 'ishtehar khan',
                   'info': 'student of here'}
    if my_id == 2 and sub == 'aryan':
        student = {'id': my_id, 'name': 'aryan khan',
                   'info': 'student of here'}
    if my_id == 3 and sub == 'yadav':
        student = {'id': my_id, 'name': 'jignesh Yadav',
                   'info': 'student of here'}
    return render(request, 'show.html', student)
