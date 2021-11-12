from django import urls
from django.urls import path
from CRUD_app import views
urlpatterns = [
    path('', views.add_show, name='add'),
    path('delete/<int:Id>', views.delete_data, name='delete'),
    path('/<int:Id>', views.update, name='update'),
]
