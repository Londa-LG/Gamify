from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import User_Registration


@login_required
def PlayerView(request):
    stats = request.user.status
    user = request.user
    content = {'status': stats, 'user': user}
    return render(request, 'User/Status.html', content)

def Registration(request):
    if request.method == 'POST':
        form = User_Registration(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request,user)
            messages.success(request,f'{username} account created')
            return redirect('/Status/')
        else:
            for msg in form.error_messages:
                messages.error(request,f'{msg}:{form.error_messages[msg]}')
    form =User_Registration()
    content = {'form': form}
    return render(request,'User/Register.html',content)

@login_required
def Logout(request):
    logout(request)
    messages.info(request,'Logout successful')
    return redirect('/')

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("Status/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    content = {'form': form}
    return render(request, 'User/Login.html', content)

