def calc_notas(*args, sit=False):
    notas = {}
    valores_recebidos = list(args)
    notas['total'] = len(valores_recebidos)
    notas['maior'] = max(valores_recebidos)
    notas['menor'] = min(valores_recebidos)
    notas['média'] = sum(valores_recebidos)/len(valores_recebidos)

    if sit == True:
        if notas['média'] > 7:
            notas['situação'] = 'BOA'
        if 4 <= notas['média'] <= 7:
            notas['situação'] = 'RAZOÁVEL'
        if notas['média'] < 4:
            notas['situação'] = 'RUIM' 


    return notas


media_da_turma = calc_notas(5.5, 2.5, 8.5, sit=True)
print(media_da_turma)