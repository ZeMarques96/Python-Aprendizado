"""
listas de listas e seus índices
"""

salas = [
    ['Maria', 'Helena'] , ['Elaine'], ['Luiz', 'João', 'Eduarda']
]
for sala, alunos in enumerate(salas):
    print(f'Os alunos que estão na sala {sala+1} são: ')
    for alunos in alunos:
        print(alunos)