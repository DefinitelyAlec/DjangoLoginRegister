# users url file
from django.urls import path
from . import views

urlpatterns = [
    # connects to the home from main url file
    path('', views.home)
]