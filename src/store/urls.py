from django.urls import path 
from . import views
urlpatterns = [
    path('', views.print_message, name = 'print message')
]