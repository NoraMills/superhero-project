from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Superhero
from django.urls import reverse

# Create your views here.


def index(request):
    all_superheroesapp = Superhero.objects.all()
    context = {
        'all_superheroesapp': all_superheroesapp
    }
    return render(request, 'superheroesapp/index.html', context)


def detail(request, superhero_id):
    selected_hero = Superhero.objects.get(pk=superhero_id)
    context = {
        'selected_hero': selected_hero
    }
    return render(request, 'superheroesapp/details.html', context)


def edit(request, superhero_id):
    superhero_delete = Superhero.objects.get(pk=superhero_id)
    context = {
        'superhero_delete': superhero_delete
    }
    return render(request, 'superheroesapp/edit.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_superpower = request.POST.get('primary_superpower')
        secondary_superpower = request.POST.get('secondary_superpower')
        catchphrase = request.POST.get('catchphrase')
        new_superhero = Superhero(name=name, alter_ego=alter_ego, primary_superpower=primary_superpower,
                                  secondary_superpower=secondary_superpower, catchphrase=catchphrase)
        new_superhero.save()
        return HttpResponseRedirect(reverse('superheroesapp:index'))
    else:
        return render(request, 'superheroesapp/create.html')
