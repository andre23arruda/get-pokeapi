from django.urls import path
from apps.pokemon.views import pokemon_abilities_view

urlpatterns = [
    path('api/pokemon/<str:pokemon_name>', pokemon_abilities_view, name='pokemon_abilities_view'),
]
