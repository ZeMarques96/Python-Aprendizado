# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'catergoria': 'Escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
    if chave != 'catergoria' 
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),

]

novo_dc = {
    chave: valor 
    for chave, valor in lista
}

s1 = {i for i in range(10)}

print(s1)
print(novo_dc)
print(dc)