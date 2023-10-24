import random
jogadores = [
    {
        'jogador': 'jogador 1',
        'dado': random.randint(1,6)
    },
    {
        'jogador': 'jogador 2',
        'dado': random.randint(1,6)
    },
    {
        'jogador': 'jogador 3',
        'dado': random.randint(1,6)
    },
    {
        'jogador': 'jogador 4',
        'dado': random.randint(1,6)
    },
    ]
rank_jogadores = sorted(jogadores, key=lambda jogador: jogador['dado'], reverse=True)

print('Valores sorteados')
for jogador in jogadores:
    for chave, valor in jogador.items():
        print(chave, valor, end= ' ')
    print()
print('Ranking:')
for jogador in rank_jogadores:
    for chave, valor in jogador.items():
        print(chave, valor, end= ' ')
    print()

