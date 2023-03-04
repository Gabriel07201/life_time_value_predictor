import pandas as pd
json = pd.read_csv('test_koRSKBP.csv')
with open(r'C:\Users\Gabriel\Desktop\Programação\life_time_value_predictor\teste.json', 'w') as arquivo:
    json.to_json(arquivo)