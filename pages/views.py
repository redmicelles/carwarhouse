from django.shortcuts import render
from .models import Team

# Create your views here.

def home(request) -> render:
    teams: Team = Team.objects.all()

    data: dict = {
        'teams': teams
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
