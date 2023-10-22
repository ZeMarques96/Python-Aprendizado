"""
# Dicionários em Python (tipo Dict)
# Dicionários são estruturas de dados tipo par de "Chave" e "Valor".
# Chaves podem ser considerados como o "índice" que vimos na lista e podem ser de tipos imutáveis
# Como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incuindo outro dicionário.
# Usamos as chaves {} - ou a classe dict para criar os dicionários
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [ 
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}  

 pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')"""

"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [ 
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

lista = () # tuple
print(type(lista))
lista = [] # list
print(type(lista))
lista = {} # dict
print(type(lista))

#lista = ['Chico', 'Bento']

#for chave, valor, in enumerate(lista):
#    print(chave, valor)
"""
pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.8,
    'endereços': [ 
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}

print(pessoa['nome'])

for chave, valor in pessoa:
    print(chave, valor)
