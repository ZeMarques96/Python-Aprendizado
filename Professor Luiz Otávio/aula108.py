"""

Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]

RESULTADO:
lista_soma = [2, 4, 6, 8]"""

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]


# ATRAVÉS DE FUNÇÃO
def somalista(l1, l2):
    menor_lista = min(len(l1), len(l2))
    return [
       l1[c] + l2[c] for c in range(menor_lista)
       
    ]

novalista = somalista(lista_a, lista_b)


# LIST COMPREHENSION
# lista_soma = [lista_a[i] +lista_b[i] for i in range(len(lista_b))]
lista_soma = [x + y for x, y in zip(lista_a,lista_b)]


print(novalista)
print(lista_soma)


