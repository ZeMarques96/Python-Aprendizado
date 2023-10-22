linhas = 3
colunas = 3
matriz = []
lista = []
for linhas in range(linhas):
    for colunas in range(colunas):
        lista.append(int(input(f'Digite um valor: [{linhas}, {colunas}]: ')))
    colunas = 3
    matriz.append(lista[:])
    lista.clear()
for linhas in matriz:
    for itens in linhas:
        print(f'[ {itens} ]', end=' ')
    print()