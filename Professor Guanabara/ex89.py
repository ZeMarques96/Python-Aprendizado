alunos = []

while True:
    nome = str(input('Digite o seu nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

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

print(f"{'nO.':<4}{'NOME':>6}{'MÉDIA':>15}")
print('-'*25)
for i, a in enumerate(alunos):
    print(f' {i:<4} {a[0]:<10} {a[2]:>6.1f}')
print('-'*25)
while True:
    resposta = int(input('Deseja ver as notas de qual aluno? (999 interrompe)'))
    if resposta >= len(alunos) and resposta != 999:
        print('Resposta inválida, aluno não existente! ')
        continue
    if resposta == 999:
        print('Programa encerrado!')
        break
    print(alunos[resposta][0], alunos[resposta][1])





# print(alunos)