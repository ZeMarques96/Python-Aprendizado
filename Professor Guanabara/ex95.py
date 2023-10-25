jogadores = []

# COLETA DE DADOS
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador: '))
    quantidade_de_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    tot_gols = 0
    for c in range(quantidade_de_jogos):
        gol = int(input(f'Quantos gols na partida {c+1}? '))
        jogador['gols'].append(gol)
    for gol in jogador['gols']:
        tot_gols += gol
    jogador['total'] = tot_gols
    jogadores.append(jogador)
    while True:
        resposta = str(input('Deseja continuar? [S/N]')).upper()
        if resposta in 'SsNn':
            break
        else:
            print('Responda apenas [S/N]')
    if resposta in 'Nn':
        break

# TABELA
print('cod ', end='')
for i in jogador.keys():
    if i != 'nome':
        print(f'{i:<13}', end='')
    else:
        print(f'{i:<15}', end='')
print()

for k, v in enumerate(jogadores):
    print(f'{k:>2}', end='')
    for s,d in v.items():
        if s == 'gols':
            print(f'  {str(d):<14}', end='')
        else:
            print(f'  {str(d):<12}', end='')
    print()


# MENU
while True:
    mostrar = int(input('Mostrar dados de qual jogador? '))
    print('-='*15)
    if mostrar == 999:
        break
    elif mostrar >= len(jogadores):
        print('Erro! JOGADOR NÃO EXISTE')
        continue
    else:
        print(f'LEVANTAMENTO DO JOGADOR {jogadores[mostrar]["nome"]}')
        for jogo,gol in enumerate(jogadores[mostrar]["gols"]):
            print(f' -> No jogo {jogo} fez {gol}')
        print('-='*15)
