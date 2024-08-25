from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('demand/', views.demand, name='demand'),
    path('inventory/', views.inventory, name='inventory'),
    path('recommendations/', views.recommendations, name='recommendations'),
]
