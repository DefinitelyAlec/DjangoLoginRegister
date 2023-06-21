from django.shortcuts import render

from django.http import HttpResponse


# Handles logic for the 'home' function
# Currently returns a basic 'hello world' page
def home(request):
    return render(request, 'users/home.html')
