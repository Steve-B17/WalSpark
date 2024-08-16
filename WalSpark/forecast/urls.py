from django.urls import path
from . import views

urlpatterns = [
    path('demand/', views.demand_forecast, name='demand_forecast'),
    path('inventory/', views.inventory, name='inventory'),
    path('recommendations/', views.recommendations, name='recommendations'),
]