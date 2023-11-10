# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos


from itertools import combinations, permutations , product

def print_comb(iterator, tam_grupo):
    print(*list(combinations(iterator, tam_grupo)), sep='\n')
    print()


def print_permutations(iterator):
    print(*list(iterator), sep='\n')
    print()


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia'
]

camisetas = [
    ['preta', 'branca'],
    ['P', 'M', 'G'],
    ['Masculino', 'Feminino'],
    ['Algodão', 'Poliéster'],
]

# print_comb(pessoas, 3)
# print_permutations(pessoas, 4)
produtos = list(product(*camisetas))
print_iter(product(*camisetas))
