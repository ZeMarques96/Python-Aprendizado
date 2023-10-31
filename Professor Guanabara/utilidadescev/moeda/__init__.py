def resumo(valor, aumento, reducao, formato=True):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço Analisado:":<20} {troca_por_comma(analisar(valor, formato))}')
    print(f'{"Dobro do preço:":<20} {troca_por_comma(dobro(valor, formato))}')
    print(f'{"Metade do preço:":<20} {troca_por_comma(metade(valor, formato))}')
    print(f'{aumento}{"% de redução:":<18} {troca_por_comma(aumentar(valor, aumento, formato))}')
    print(f'{reducao}{"% de redução:":<18} {troca_por_comma(diminuir(valor, reducao, formato))}')
    print('-' * 30)




def analisar(valor, formatar= False):
    valor = f'{valor:.2f}'
    valor = moeda(valor, formatar)
    return valor
     



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
        valor *= 2
        return f'{valor:.2f}'

def diminuir(valor, qnt, formatar=False):
    qnt = ((qnt / 100) - 1) * -1
    
    if formatar:
        valor = valor * qnt
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        valor = valor * qnt
        return f'{valor:.2f}'

def aumentar(valor, qnt, formatar=False):
    qnt = (qnt/100) + 1
    
    if formatar:    
        valor = valor * qnt
        valor = f'{valor:.2f}'
        valor = moeda(valor)
        return valor
    else:
        valor = valor * qnt
        return f'{valor:.2f}'

def moeda(valor, formato=True):
    if formato:
        return f'R$ {valor}'
    else:
        return valor

def troca_por_comma(valor, formato=True):
    if formato:    
        valor = valor.replace('.', ',')
        return valor
    else:
        return valor
