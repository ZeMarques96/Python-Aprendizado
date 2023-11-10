#groupby - agrupando valores (itertools)

from itertools import groupby
import copy

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])


for chave, grupo in grupos:
    print(f'Alunos com Notas: {chave}')
    for aluno in grupo:
        for chave, valor in aluno.items():
            print(f'{chave}: {valor}', end=' ')
        print()




