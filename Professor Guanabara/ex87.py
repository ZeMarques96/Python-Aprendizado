linhas = 3
colunas = 3
# matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz = []
tot_par = 0
tot_terceira_coluna = 0
maior_valor_segunda_coluna = 0

for linha in range(linhas):
    lista = []
    for coluna in range(colunas):
        lista.append(int(input(f'Digite um valor: [{linha}, {coluna}]: ')))
        if lista[coluna] % 2 == 0:
            tot_par += lista[coluna]
    matriz.append(lista[:])

for linha in matriz:
    for coluna in range(len(linha)):
        if coluna == 2:
            tot_terceira_coluna += linha[coluna]
        if linha == matriz[1] and linha[coluna] > maior_valor_segunda_coluna:
            maior_valor_segunda_coluna = linha[coluna]



        
    # print()
print(f'A soma dos valores pares é de : {tot_par}')
print(f'A soma dos valores da terceira coluna é de : {tot_terceira_coluna}')
print(f'O maior valor da segunda linha é de : {maior_valor_segunda_coluna}')