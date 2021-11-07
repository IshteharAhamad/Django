from django.urls import path
from . import views
urlpatterns = [
    path('reg/', views.detail),
    path('success/', views.success),
]
