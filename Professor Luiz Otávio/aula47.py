import os

palavra_secreta = 'perfume'
letras_acertadas = ''
qnt_tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ').lower()

    if len(letra_digitada) > 1:
       print('Digite Apenas uma letra')
       continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    qnt_tentativas += 1
    print(f'Essa é a tentativa de número: {qnt_tentativas}')
    if palavra_formada == palavra_secreta:
        os.system('cls')
        break
    print(palavra_formada)
print(f'PARABÉNS, VOCÊ GANHOU NA TENTATIVA DE NÚMERO: {qnt_tentativas}\n A palavra secreta é {palavra_secreta}')
    
    

        
