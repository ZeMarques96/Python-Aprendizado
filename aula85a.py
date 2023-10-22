"""def divfn(x , y):
    return x / y


valores = [1, 2, 3, 4, 5]

valores_divididos = [divfn(valor, 2) for valor in valores]
valores_multiplicados = [valor * 2 for valor in valores]
valores_potencia = [valor ** 2 for valor in valores]

print(valores_divididos)
print(valores_multiplicados)
print(valores_potencia)
"""

"""lista = [
    (x,y)
    for x in range(1,6)
    for y in range(1,6)
    if x == y
]
"""


"""nomes = ['Luiz', 'Maria', 'Helena', 'Joana', 'Felipe']

lista = [
    f'{nome[:-1].lower()+nome[-1].upper()}'  for nome in nomes
    ]

reverso = [
    nome[::-1] for nome in nomes
]

print(reverso)
print(lista)"""

numeros = [(numero, numero **2) for numero in range(11)]

flat = [
    y for x in numeros for y in x
]
print(flat)
print(numeros)