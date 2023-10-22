# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def mostra_lista(lista):
    for item in lista:
        print(item)
    



produtos_corrigidos = [
    {**produto, 'preco': f"{produto['preco'] * 1.1:.2f}"} # round(produto['preco'] * 1.1 , 2)
    for produto in produtos
    
]

produtos_corrigidos_copia = copy.deepcopy(produtos_corrigidos)

produtos_ordenados_por_nome = sorted(produtos_corrigidos_copia, key=lambda item : item['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(produtos_corrigidos, key=lambda item: item['preco'])

produtos_ordenados_por_preco_dois = sorted(copy.deepcopy(produtos), key=lambda p: p['preco'])


# mostra_lista(produtos_ordenados_por_nome)
# print()
# mostra_lista(produtos_ordenados_por_preco)
# print()
# mostra_lista(produtos_ordenados_por_preco_dois)

print(*produtos_corrigidos, sep='\n')
print()
print(*produtos, sep='\n')

# mostra_lista(produtos)
# mostra_lista(produtos_corridigos)