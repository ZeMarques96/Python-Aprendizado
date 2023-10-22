import random
numero_de_jogos = 10
lista = []
jogo = []
for c in range(numero_de_jogos):
    jogo = []
    while len(jogo) <= 6:
        numero = random.randint(1, 60)
        if numero not in jogo:
            jogo.append(numero)
            jogo = sorted(jogo)
    lista.append(jogo[:])

for jogo in range(len(lista)):
    print(f'Jogo {jogo+1}: {lista[jogo]}')