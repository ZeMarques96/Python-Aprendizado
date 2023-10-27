def voto(nascimento):
    import datetime
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - nascimento
    if 18 <= idade <= 65:
        return  f'Com {idade} Anos o voto é OBRIGATÓRIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} Anos o voto é OPCIONAL.'
    else:
        return f'Com {idade} Anos NÃO VOTA.'
    
ano_nascimento = int(input('Ano de Nascimento: '))

print(voto(ano_nascimento))