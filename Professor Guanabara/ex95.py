# jogadores = [
#     {
#         'nome': 'Joel',
#         'gols': [3, 2],
#         'total': 5,
#     },
#     {
#         'nome': 'Pedrão',
#         'gols': [2, 0, 4],
#         'total': 6,
#     },
#     {
#         'nome': 'Wesley',
#         'gols': [0, 0, 0, 0],
#         'total': 0,
#     },
# ]
jogadores = []

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
        resposta = str(input('Deseja continuar? [S/N]'))
        if resposta in 'Ss':
            break
        if resposta in 'Nn':
            break
        else:
            print('Resposta inválida')
    if resposta in 'Nn':
        break

espaco = ' '
espaco = len(jogadores[0]['gols'])
for jogador in jogadores:
    for valores in jogador.values():
        if type(valores) is list and len(valores) > espaco:
            espaco = len(valores)

print(f' {"cod":<5} {"nome":>6}{"gols":>10} {"total":>15}')
for c,jogador in enumerate(jogadores):
    print(f'  {c:<7}{jogador["nome"]:<10}{jogador["gols"]}', end ='')
    if len(jogador["gols"]) <= espaco:
        espaco_atual = espaco - len(jogador['gols'])
        espaco_atual = ' ' * (espaco_atual * 3 )        
    print(f'{espaco_atual}{jogador["total"]:>5}')

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
