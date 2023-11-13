from functools import partial


#map - para mapear dados

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


aumentar_dez_porcento = partial(aumentar_porcentagem, porcentagem=1.1)


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]



#RELEMBRANDO DICTIONARY COMPREHENSION
# produtos_caros = [
#     {'nome': produto['nome'], 'preco': produto['preco']}
#     for produto in produtos
#     if produto['preco'] > 50
# ]

# USANDO PARTIAL

# novos_produtos = [
#     {**p, 
#      'preco' : aumentar_dez_porcento(p['preco'])} for p in produtos
# ]
# ----------------------------------------------------------------------------------
# TESTE
# novos_produtos = [
#     {**p, 
#      'preco' : aumentar_porcentagem(p['preco'])} for p in produtos
# ]

def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumentar_dez_porcento(produto['preco'])
    }

novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)




print_iter(produtos)
print()
print_iter(novos_produtos)