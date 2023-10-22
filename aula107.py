# Exercícios - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem.
# Use todos os valores da menor lista.
# Ex. :
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

estados = ['BA', 'SP', 'MG', 'RJ']
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
juntos = []



def merge_lista(cidades, estados):
    tamanho_da_menor_lista = min(len(cidades), len(estados))

    for x in range(tamanho_da_menor_lista):
        cidade = cidades[x]   
        estado = estados[x]
        juntos.append((cidade,estado))
    return juntos

lista_nova = merge_lista(cidades, estados)
print(lista_nova)