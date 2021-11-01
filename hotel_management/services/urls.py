from django.urls import path
from . import views
urlpatterns = [
    path('hello/', views.services),
    path('king',views.king),
]