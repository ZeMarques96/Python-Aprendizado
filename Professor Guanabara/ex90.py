aluno = {}
aluno['nome'] = 'José'
aluno['média'] = 8
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] <= 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')