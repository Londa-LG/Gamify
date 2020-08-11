from django.shortcuts import render


def PlayerView(request):
    return render(request,'status/Status.html')