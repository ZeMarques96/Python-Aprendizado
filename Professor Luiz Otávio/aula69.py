"""
agr - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)

lembre-se de desempacotamento
# x, y * resto = 1, 2, 3, 4
print(x, y, resto)"""


def soma(*args):
    total = 0
    print(args)
    for soma in args:
        total += soma
    return total

#       0 1 2 3 4 5 6
tupla = 1,2,3,4,5,6,7
lista = []
lista = list(tupla)
print(type(tupla), type(lista))
#print(soma(numeros))
coisa = soma(*tupla)
print(tupla.index(3))

print(*tupla)
print(sum(tupla))