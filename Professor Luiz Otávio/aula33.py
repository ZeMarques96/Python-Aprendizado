hora = input('Que horas são? ')

try:
    hora = int(hora)

    if hora >= 6 and hora <= 12:
        print('Bom Dia')
    elif hora >=13 and hora <=18:
        print('Boa Tarde')
    elif hora >= 19 and hora <= 24 or hora < 6:
        print('Boa Noite')
    else:
        print('HORA INVÁLIDA!')
except:
    print('Apenas números inteiros')