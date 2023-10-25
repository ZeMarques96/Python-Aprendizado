import random

def somapar(lista):
    soma = 0
    print(f'Somando os valores PARES da lista: {lista}', end=',')
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'temos {soma}')

def sorteia(lista):
    numero = 0
    for x in range(5):
        numero = random.randint(1,10)
        lista.append(numero)
    return (lista)

numeros = []
sorteia(numeros)
somapar(numeros)