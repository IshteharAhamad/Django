from django.urls import path
from  . import views
urlpatterns = [
    path('Dj/', views.django),
]