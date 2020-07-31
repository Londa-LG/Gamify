from django.shortcuts import render
from django.http import HttpResponse

def Registration(request):
    return HttpResponse('<h1>This is the Registration and Sign up Page</h1>')

def Login(request):
    return HttpResponse('<h1>Welcome to the login page now LogIn</h1>')