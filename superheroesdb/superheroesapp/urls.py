from django.urls import path
from . import views


app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='details'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('remove/', views.remove, name='remove')
]
