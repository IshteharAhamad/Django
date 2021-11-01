from django.urls import path
from . import views
#from django.urls import fees
urlpatterns = [
    path('fees/',views.Fees ),
    path('fes/',views.Fees1),
]