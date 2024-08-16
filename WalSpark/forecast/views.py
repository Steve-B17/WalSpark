from django.shortcuts import render

def demand_forecast(request):
    return render(request, 'forecast/demand_forecast.html')

def inventory(request):
    return render(request, 'forecast/inventory.html')

def recommendations(request):
    return render(request, 'forecast/recommendations.html')
