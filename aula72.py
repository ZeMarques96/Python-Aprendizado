"""
Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável.

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar"""


def multiplicador(*args):
    total_multiplicacao = 1
    for numeros in args:
        total_multiplicacao *= numeros
    return total_multiplicacao


resultado = multiplicador(1,2,3,4,5)
print(resultado)