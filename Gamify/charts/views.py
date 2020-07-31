from django.shortcuts import render
from django.http import HttpResponse

def AllCharts(request):
    return HttpResponse('<h1>This is the charts page</h1>')
