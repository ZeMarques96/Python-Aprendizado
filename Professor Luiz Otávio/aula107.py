# Exercícios - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex. :
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]
from itertools import zip_longest


estados = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
juntos = []


def unir_lista(lista1, lista2):
    tamanho_menor_lista = min(len(lista1), len(lista2))
    return [
        (lista1[c], lista2[c]) for c in range(tamanho_menor_lista)
    ]


listas_unidas = unir_lista(cidades, estados)
print(listas_unidas)

print(list(zip(cidades, estados)))
print(list(zip_longest(cidades, estados)))
print(list(zip_longest(cidades, estados, fillvalue='SEM CIDADE')))