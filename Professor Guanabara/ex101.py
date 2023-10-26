import datetime

def voto(nascimento):
    idade = ano_atual - nascimento
    if 18 <= idade <= 65:
        estado = f'Com {idade} Anos o voto é OBRIGATÓRIO.'
    elif idade > 65:
        estado = f'Com {idade} Anos o voto é OPCIONAL.'
    else:
        estado = f'Com {idade} Anos NÃO VOTA.'
    return estado


ano_atual = datetime.datetime.now().year

ano_nascimento = int(input('Ano de Nascimento: '))

estado = voto(ano_nascimento)

print(estado)