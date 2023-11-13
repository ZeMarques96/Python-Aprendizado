# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis para dividir problemas grandes em partes menores 
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
3# - Um caso recursivo que resolver o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

import sys

#sys.setrecursionlimit(1200)

# def recursiva(inicio = 0 , fim = 4):
#     # Caso Recursivo
#     # contar até chegar ao fim
#     print(inicio, fim)

#     if inicio >= fim:
#         return inicio
    
#     inicio += 1

#     return recursiva(inicio, fim)

# print(recursiva())


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))