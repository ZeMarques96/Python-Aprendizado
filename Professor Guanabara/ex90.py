aluno = {}
aluno['Nome'] = 'José'
aluno['Média'] = 7.5
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')