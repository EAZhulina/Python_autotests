import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5875a0c2faff607bcda7c1241fdf3f09'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Чейзи",
    "photo_id": 5
}

body_put_name = {
    "pokemon_id": "72299",
    "name": "Боня",
    "photo_id": 5
}

body_add_pokeball = {
    "pokemon_id": "72299"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_put_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_name)
print(response_put_name.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)