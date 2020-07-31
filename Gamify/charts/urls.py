
from django.urls import path
from .views import AllCharts

urlpatterns = [
    path('', AllCharts, name='all'),
]
