import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5875a0c2faff607bcda7c1241fdf3f09'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}
TRAINER_ID = '4998'

def test_status():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200
    
def test_trainer_name():
    response_trainer_name = requests.get(url = f'{URL}/me', params ={'trainer_id' : TRAINER_ID}, headers = HEADER)
    assert response_trainer_name.json()["data"][0]["trainer_name"] == "Ketish"