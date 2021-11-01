from django.urls import path
from  . import views
urlpatterns = [
    path('co/', views.pythn),
    path('cor/', views.DJ),
    path('img/', views.Image),
    path('ha/', views.inner),
]