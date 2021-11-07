from django.contrib import admin
from .models import Student
# using decorator


@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    list_display = ('s_id', 'roll_No', 'name', 'email', 'mobile', 'course')


#admin.site.register(Student, Student_Admin)
