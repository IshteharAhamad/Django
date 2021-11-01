from django.urls import path
from . import views
urlpatterns = [
    path('dj/',views.course),
    path('py/',views.coursepy),
]