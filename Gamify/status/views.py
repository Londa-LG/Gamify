from django.shortcuts import render
from User.models import Status
from django.contrib.auth.models import User


def PlayerView(request):
    user1 = User.objects.get(username='Londa')
    stats = Status.objects.get(user=user1)
    content = {'status': stats }
    return render(request,'status/Status.html',content)