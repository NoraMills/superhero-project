from django.urls import path
from . import views

app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index')
]
