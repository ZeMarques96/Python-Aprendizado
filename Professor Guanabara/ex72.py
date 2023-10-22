numeros_por_extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    resposta_usuario = int(input('Digite um número de 0 a 20: '))
    if 0 <= resposta_usuario <= 20:
        break
    else:
        print('Tente novamente. ', end='')


print(numeros_por_extenso[resposta_usuario])