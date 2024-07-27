from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from django.http import HttpResponse, HttpRequest
from django.contrib import messages

# Create your views here.





def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('/')




