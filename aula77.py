# Manipulando Chaves e valores em dicionário


"""pessoa = {}


pessoa['nome'] = 'José Francisco'
print(pessoa)"""

"""
# Métodos úteis dos dicionários em Python

# len - Quantas Chaves
# keys - iterável com as chaves
# values - iterável com os valores 
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda',

}
"""print(pessoa)
print(pessoa.__len__())
print(len(pessoa))
print(pessoa.keys())
print(pessoa.values())"""

for valores in pessoa.values():
    print(valores)


print(pessoa.items())

for chave, valor in pessoa.items():
    print(chave, valor)

print('---------------------')