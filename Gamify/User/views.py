from django.shortcuts import render
from django.http import HttpResponse
from .forms import User_Registration
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .lib import CreateInventory, CreatePlayer, BasicItem


def Registration(request):
    if request.method == 'POST':
        form = User_Registration(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            messages.success(request,f'{username} account created')
            CreatePlayer(username)
            CreateInventory(username)
            BasicItem(username)
        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}:{form.error_messages[msg]}')
    form =User_Registration()
    content = {'form': form}
    return render(request,'User/Register.html',content)

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request,'Login successful')
            else:
                for msg in form.error_messages:
                    messages.error(request,f"{msg}:{form.error_messages[msg]}")
    form = AuthenticationForm()
    content = {'form': form}
    return render(request,'User/Login.html',content)

def logout(request):
    logout(request)
    messages.info(request,'Logout successful')
    return HttpResponse('<h1>This is the Logout Page')