

def calc_notas(*args, sit=False):
    notas = {}
    maior = 0
    valores_recebidos = list(args)
    notas['total'] = len(valores_recebidos)
    tot_notas = 0

    for c in range(len(valores_recebidos)):
        if c == 0:
            menor = valores_recebidos[c]
        if valores_recebidos[c] > maior:
            maior = valores_recebidos[c]
            notas['maior'] = maior
        if valores_recebidos[c] <= menor:
            menor = valores_recebidos[c]
            notas['menor'] = menor
    
    for valores in valores_recebidos:
        tot_notas += valores
    media = tot_notas/ len(valores_recebidos)
    notas['média'] = media
    
    if sit == True:
        if notas['média'] > 7:
            notas['situação'] = 'BOA'
        if 4 <= notas['média'] <= 7:
            notas['situação'] = 'RAZOÁVEL'
        if notas['média'] < 4:
            notas['situação'] = 'RUIM' 

    return notas


# def mostro_dict(**kwargs):
#     for chave,valor in kwargs.items():
#         print(chave ,valor)



media_da_turma = calc_notas(3.5, 2, 6.5, 2, 7, 4, sit=True)
print(media_da_turma)
# mostro_dict(**media_da_turma)

