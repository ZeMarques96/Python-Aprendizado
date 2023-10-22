
"""nome = 'José Francisco'
tamanho = len(nome) * -1
controle = -1
while controle >= tamanho  :
    print(nome[controle], end= '\n')
    controle -= 1
"""    
nome = 'José Francisco'
controle = 0
nova_string = '*'
while controle < len(nome):
    nova_string += nome[controle] + '*' 
    controle += 1
print(nova_string)