from django.urls import path
from . import views
urlpatterns = [
    path('fees/', views.Pf),
    path('fee/', views.Df),
    path('some/', views.join),
]