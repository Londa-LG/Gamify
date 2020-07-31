from django.shortcuts import render
from django.http import HttpResponse

def Character(request):
    return HttpResponse('<h1>This is the character homepage</h1>')


