"""
# Exercícios 
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.
"""

def multiplicacao(multiplicador):
    def multiplicar(numero):
        return multiplicador * numero
    return multiplicar

dobro = multiplicacao(2)
triplo = multiplicacao(3)
quadruplo = multiplicacao(4)
quintuplo = multiplicacao(5)

numero = int(5)

print(dobro(10))
print(triplo(numero))
print(quadruplo(numero))
print(quintuplo(numero))