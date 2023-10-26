

def cad_jogador(nome='', gols = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = 0
    sentenca = f'O jogador {nome} fez {gols} Gols no campeonato.'

    return sentenca

nome = input('Nome do Jogador: ')
qnt_gols = input('Número de Gols:')
print(cad_jogador(nome, qnt_gols))