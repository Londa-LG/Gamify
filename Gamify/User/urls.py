from django.urls import path
from .views import Registration, Login

urlpatterns = [
    path('login/',Login,name='login'),
    path('', Registration,name='register'),
]
