import json
import os

# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'endereços': [
#         {'rua': 'R1', 'numero' : 32},
#         {'rua': 'R2', 'numero' : 55},
#     ],
#     'altura' : 1.8,
#     'numeros_preferidos' : (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as file:
#     json.dump(pessoa, file, ensure_ascii=False,
#               indent=2)


with open('aula117.json', 'r', encoding='utf8') as file:
    pessoa = json.load(file)
    # print(pessoa)
    # print(type(pessoa))