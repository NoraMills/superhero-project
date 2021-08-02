from django.shortcuts import render
from django.http import HttpResponse
from .models import Superhero

# Create your views here.


def index(request):
    all_superheroesapp = Superhero.objects.all()
    return render(request, 'superheroesapp/index.html')
