# Função Lambda em Python
# A função é uma função como qualquer outra em Python. Porém, são funções anônimas,
# que contém apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.

# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'Miranda'},
#     {'nome': 'Maria', 'sobrenome': 'Oliveira'},
#     {'nome': 'Daniel', 'sobrenome': 'Silva'},
#     {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
#     {'nome': 'Aline', 'sobrenome': 'Souza'},

# ]

lista = [
    {'nome': 'Luiz', 'sobrenome': 'Miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},

]

# def orderna(item):
#     return item ['nome']

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()
    
exibir(l1)
exibir(l2)