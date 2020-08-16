from django.urls import path
from .views import Registration, Login, PlayerView, Logout, Challenge

app_name='User'

urlpatterns = [
    path('', Login, name='login'),
    path('Register/', Registration, name='register'),
    path('Status/', PlayerView, name='status'),
    path('Logout/', Logout, name='logout'),
    path('Comp/', Challenge, name='complete'),
]
