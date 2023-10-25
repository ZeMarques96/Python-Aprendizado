import random

def sorteia(lista,tamanho):
    for x in range(tamanho):
        valor = random.randint(1,10)
        lista.append(valor)
    return lista
lista = []
sorteia(lista, 10)
print(lista)
print(len(lista))