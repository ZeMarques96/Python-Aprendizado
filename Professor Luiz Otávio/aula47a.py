palavra_secreta = 'perfume'
letras_acertadas = ''
qnt_tentativas = 0

while True:
    palpite = input('Digite uma letra: ').lower()
    qnt_tentativas += 1
    if len(palpite) > 1:
        print('Digite apenas uma letra') 
    
    if palpite in palavra_secreta:
        letras_acertadas += palpite
    palavra_formatada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += '*'
    
    print(f'Palavra Formatada: {palavra_formatada}')
    if palavra_formatada == palavra_secreta:
        break
print('Parabéns, Você Ganhou!')
print(f'A palavra secreta era {palavra_formatada}')
print(f'O número de tentativas foram: {qnt_tentativas}')
