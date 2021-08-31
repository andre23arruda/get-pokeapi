from django.http import Http404
from django.http import JsonResponse

import requests


def pokemon_abilities_view(request, pokemon_name: str):
    '''Redirect short url to long url'''
    base_url = r'https://pokeapi.co/api/v2/pokemon'
    try:
        response = requests.get(f'{ base_url }/{ pokemon_name }')
        pokemon_info = response.json()
        pokemon_abilities = pokemon_info['abilities']
        pokemon_abilities_ordered = sorted([ability['ability']['name'] for ability in pokemon_abilities])

        return JsonResponse({
            'abilities': pokemon_abilities_ordered
        })
    except:
        Http404('Desculpe, aconteceu algum erro!')
