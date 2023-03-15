from django.shortcuts import render
from .models import Team
from cars.models import Car

# Create your views here.

def home(request) -> render:
    teams: Team = Team.objects.all()
    # featured_cars: Car = Car.objects.\
    #     order_by('-created_date').\
    #     filter(is_featured=True)
    all_cars: Car = Car.objects.\
        order_by('-created_date')
    data: dict = {
        'teams': teams,
        'featured_cars': all_cars.filter(is_featured=True),
        'all_cars': all_cars
    }
    return render(request, 'pages/home.html', data)

def about(request) -> render:
    teams: Team = Team.objects.all()
    data: dict = {
        "teams": teams
    }
    return render(request, 'pages/about.html', data)

def services(request) -> render:
    return render(request, 'pages/services.html')

def contact(request) -> render:
    return render(request, 'pages/contact.html')
