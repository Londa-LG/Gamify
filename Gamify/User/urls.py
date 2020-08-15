from django.urls import path
from .views import Registration, Login, PlayerView, Logout

app_name='User'

urlpatterns = [
    path('', Login, name='login'),
    path('Register/', Registration, name='register'),
    path('Status/', PlayerView, name='status'),
    path('Logout/', Logout, name='logout'),
]
