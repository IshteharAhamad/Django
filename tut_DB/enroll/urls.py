from django.urls import path
from . import views
urlpatterns = [
    path('data/', views.display),
    path('detail/', views.details),
]
