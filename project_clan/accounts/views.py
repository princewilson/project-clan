from django.shortcuts import render, redirect
from project_clan import passwords
import requests
from django.contrib.auth import logout


# Create your views here.
def signup(request):
    return render(request, './accounts/signup.html')

def callback(request):
    if request.user.is_authenticated:
        return render(request, './accounts/dashboard.html')
    return render(request, './base.html')

def logout_user(request):
    logout(request)
    return redirect('base')