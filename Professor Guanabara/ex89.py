alunos = [
        # ['Aluno 1', [6.7, 4.5], 5.8], 
        # ['Aluno 2', [7.3,  8.2], 6.2], 
        # ['Aluno 3', [ 6.1, 4.5], 3.8], 
        ]
while True:
    aluno = []
    notas = []
    nome = str(input('Digite o seu nome: '))
    aluno.append(nome)
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    notas.append(nota1)
    notas.append(nota2)
    media = (nota1 + nota2) / 2
    aluno.append(notas)
    aluno.append(media)
    alunos.append(aluno)
    while True:
        resposta = str(input('Deseja continuar? [S/N]'))
        if resposta in 'Nn':
            break
        elif resposta in 'Ss':
            break
        else:
            print('Resposta inválida!!')
    if resposta in 'Nn':
        break

print(f"No.    Nome     {'MÉDIA':>15}")
print('-'*30)
for i in range(len(alunos)):
    print( f'{i:<5}' , end=' ')
    for info in range(len(alunos[i])):
        if info == 0:
            print(f"{alunos[i][info]:>5}", end='  ')
        if info == 2:
            print( f"{alunos[i][info]:>15}" , end= '')
    print('\n')
while True:
    resposta = 0
    resposta = int(input('Deseja ver as notas de qual aluno? '))
    if resposta >= len(alunos) and resposta != 999:
        print('Resposta inválida, aluno não existente! ')
        continue
    if resposta == 999:
        print('Programa encerrado!')
        break
    print(alunos[resposta][0], alunos[resposta][1])





# print(alunos)