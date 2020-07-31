from django.urls import path
from .views import Registration, Login

urlpatterns = [
    path('',Login,name='login'),
    path('register/', Registration,name='register'),
]
