# a = 2, 5, 4
# b = 5, 8, 1, 2
# c = b + a 
# print(c)
# print(c.index(2))

# Defina o número de linhas e colunas da matriz
linhas = 3
colunas = 3

# Inicialize uma lista vazia que representará a matriz
matriz = []

# Preencha a matriz com valores
for i in range(linhas):
    linha = []  # Inicialize uma nova lista para cada linha
    for j in range(colunas):
        valor = int(input(f'Digite o valor da posição ({i+1}, {j+1}): '))
        linha.append(valor)  # Adicione o valor à linha
    matriz.append(linha)  # Adicione a linha à matriz

# Exiba a matriz
for linha in matriz:
    print(linha)