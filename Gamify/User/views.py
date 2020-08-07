from django.shortcuts import render
from django.http import HttpResponse
from .lib import Date

def Registration(request):
    reg_date = Date()
    return render(request,'User/Register.html')

def Login(request):
    return render(request,'User/Login.html')