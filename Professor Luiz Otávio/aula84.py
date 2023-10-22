# List comprehension em python
# list comprehensiom é uma forma rápida para criar listas a partir de iteráveis.

print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

listacomprehension = [
    numero * 2 
    for numero in range(1, 11)
]
print(listacomprehension)

# Mapeamento de dados em list comprehension
print()
print()

produtos = [
    {'nome' : 'p1' , 'preco' : 20 ,},
    {'nome' : 'p2' , 'preco' : 10 ,},
    {'nome' : 'p3' , 'preco' : 30 ,},
]

print(*produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print()

print(*novos_produtos, sep='\n')


numeros_pares = [
    numero
    #if numero % 2 == 0 else numero
    for numero in range(100)
    if numero % 2 == 0  
]
print(numeros_pares)