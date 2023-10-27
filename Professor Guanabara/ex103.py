

def cad_jogador(nome='<desconhecido>', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} Gols no campeonato.'

    

nome = input('Nome do Jogador: ')
qnt_gols = input('Número de Gols:')

print(cad_jogador(nome, qnt_gols))
print(cad_jogador(gols=qnt_gols))