
from django.urls import path
from .views import Character

urlpatterns = [
    path('', Character,name='home'),
]
