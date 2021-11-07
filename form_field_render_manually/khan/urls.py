from django.urls import path
from khan import views
urlpatterns = [
    path('reg/', views.showdetails),
]
