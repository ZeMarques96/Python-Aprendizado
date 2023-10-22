frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'.lower()
print(frase)

i= 0
letra_mais_aparece = 0
letra_que_mais_apareceu = ''
quantas_x_apareceu = 0
letra_atual = ''



while i < len(frase):
    letra_atual = frase[i]
    quantas_x_apareceu = frase.count(letra_atual)
    if quantas_x_apareceu > letra_mais_aparece and letra_atual != ' ':
        letra_mais_aparece = quantas_x_apareceu
        letra_que_mais_apareceu = letra_atual
    i +=1
print(f'A letra que mais aparece na frase é a letra "{letra_que_mais_apareceu}" e aparece {letra_mais_aparece} vezes.')