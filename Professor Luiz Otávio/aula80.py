"""

Exercício 
Crie uma função que encontra o primeiro duplicado considerando o ssegundo número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda ocorrência do número, ou seja
    o número duplicado em si.
    Exemplo:
        [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
    Se não encontrar duplicados na lista, retorne -1
    """

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], # -1
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8], # 9
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7], # 2
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9], # 7
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7], # 8
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9], # 2
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1], # 2
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3], # 1
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7], # 1
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1], # 2
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7], # 
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def numero_repetidos(lista):
    controle_de_repetidos = set()
    lista_de_numeros_repetidos = []
    for controle in lista:
        mais_de_uma_vez = 0
        for numero in lista:
            if controle == numero:
                mais_de_uma_vez +=1
            if controle == numero and mais_de_uma_vez > 1:
                controle_de_repetidos.add(numero)
    lista_de_numeros_repetidos = controle_de_repetidos
    lista_de_numeros_repetidos = sorted(lista_de_numeros_repetidos)

    return lista_de_numeros_repetidos

def segunda_ocorrencia(repetidos, lista):
    primeira_ocorrencia = 0
    slots = len(lista)
    for controle_repetidos in repetidos:
        repete_qnt = 0
        for numeros in lista:
            if controle_repetidos == numeros:
                repete_qnt += 1
            if repete_qnt >= 1 and controle_repetidos != numeros:
                repete_qnt += 1
            if controle_repetidos == numeros and repete_qnt > 1 and repete_qnt < slots:
                slots = repete_qnt
                primeira_ocorrencia = controle_repetidos
                break
    if primeira_ocorrencia == 0:
        primeira_ocorrencia = -1
    return primeira_ocorrencia 

for verificar in range(len(lista_de_listas_de_inteiros)):
    lista = numero_repetidos(lista_de_listas_de_inteiros[verificar])
    resultado = segunda_ocorrencia(lista, lista_de_listas_de_inteiros[verificar])
    print(resultado)




