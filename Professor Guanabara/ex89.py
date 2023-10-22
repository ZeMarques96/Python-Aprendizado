alunos = [
        ['Aluno 1', ['nota 1', 'nota 2'], ['Média']], 
        ['Aluno 2', ['nota 1', 'nota 2'], ['Média']],
        ['Aluno 3', ['nota 1', 'nota 2'], ['Média']],
        ]
# print(alunos[0][0])
# print(alunos[0][1])
# print(alunos[0][2])
# print(alunos[0][1][1])
for aluno in alunos:
    for chave in range(len(aluno)):
        if chave == 0:
            aluno[chave] = str(input('Digite o seu nome: '))
            print(aluno[chave])
        if chave == 1:
            for nota in range(len(aluno[chave])):
                aluno[chave][nota] = float(input(f'Nota {nota + 1}:'))
                print(nota)

print(alunos)