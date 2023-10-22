"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adciona um item ao final da lista 
    insert - Adciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
     + - concatena listas
Create Read Update Delete 
Criar, Ler  ,Alterar , Apagar = lista[i] (CRUD)"""

"""lista = [12, 'josé', 3, 4, 'Chama']
lista[1] = lista[1].upper()
print(len(lista), lista[-1])
lista.insert(-1, 'ultimo')
lista.append('por append')
print(lista)"""

"""lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c =[]
# lista_c.extend(lista_a,lista_b) pega só um argumento
print(lista_c)"""

lista_a = ['Luiz' , 'Maria']
lista_b = lista_a

lista_b[0] = 'Chico'
print(lista_b)