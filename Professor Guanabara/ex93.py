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
print()
print()
print(f' O jogador {jogador["nome"]} jogou {quantidade_de_jogos} partidas.')
for partida, gol in enumerate(jogador['gols']):
    print(f' -> Na partida {partida+1}, fez {gol} gols.')
print(f"Foi um total de {jogador['total']} gols.")