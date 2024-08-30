from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'forecasts/home.html')

def demand(request):
    return render(request, 'forecasts/demand_forecasting.html')

def inventory(request):
    return render(request, 'forecasts/inventory.html')

def recommendations(request):
    return render(request, 'forecasts/recommendation.html')