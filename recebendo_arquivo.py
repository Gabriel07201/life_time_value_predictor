import requests
import json
import pandas as pd


import csv

with open(r'C:\Users\Gabriel\Desktop\Programação\life_time_value_predictor\teste.json', 'rb') as arquivo:
    response = requests.post("https://api-cltv-portfolio.up.railway.app/predict/", files={"file": arquivo})


json_data = json.loads(response.content.decode('utf-8'))

# abrir o arquivo JSON para escrita
with open('exemplo.json', 'w') as f:
    json.dump(json_data, f)