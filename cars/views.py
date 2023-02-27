from django.shortcuts import render

# Create your views here.

def cars(request)->render:
    return render(request, 'cars/cars.html')
