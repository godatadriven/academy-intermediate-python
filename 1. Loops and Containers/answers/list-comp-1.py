import pandas as pd

expected_columns = ['id', 'name', 'type', 'hp', 'attack', 'defense', 'special_atk', 'speed', 'legendary']

pokemon = pd.read_csv('data/pokemon.csv')

unexpected = [col for col in pokemon.columns if col not in expected_columns]
len(unexpected), unexpected