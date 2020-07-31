from django.shortcuts import render
from django.http import HttpResponse

def Registration(request):
    return render(request,'User/Register.html')

def Login(request):
    return render(request,'User/Login.html')