def resumo(valor, aumento, reducao, formato=True):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<20} {troca_por_coma(moeda(valor))}')
    print(f'{"Dobro do preço:":<20} {troca_por_coma(dobro(valor, formato))}')
    print(f'{"Metade do preço:":<20} {troca_por_coma(metade(valor, formato))}')
    print(f'{aumento}{"% de redução:":<18} {troca_por_coma(aumentar(valor, aumento, formato))}')
    print(f'{reducao}{"% de redução:":<18} {troca_por_coma(diminuir(valor, reducao, formato))}')
    print('-' * 30)




def metade(valor, formatar=False):
    if formatar:
        valor = valor / 2
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        valor = valor /2
        return f'{valor:.2f}'

def dobro(valor, formatar=False):
    if formatar:
        valor = valor *2
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        return valor

def diminuir(valor, qnt, formatar=False):
    qnt = ((qnt / 100) - 1) * -1
    
    if formatar:
        valor = valor * qnt
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        return valor

def aumentar(valor, qnt, formatar=False):
    qnt = (qnt/100) + 1
    
    if formatar:    
        valor = valor * qnt
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        return valor

def moeda(valor):
    return f'R${valor}'

def troca_por_coma(valor):
    valor = valor.replace('.', ',')
    return valor