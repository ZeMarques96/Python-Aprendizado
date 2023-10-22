"""

Clousure e funções que retornam outras funções.
"""

def saudacao (saudacao, nome):
    return f'{saudacao}, {nome}'

nome = input('Qual o seu nome? ')
hora = input('Que horas são: ')

hora = int(hora)

if hora < 6 or hora > 18:
    cumprimento = 'Boa Noite'
elif hora > 6 and hora < 12:
    cumprimento = 'Bom Dia'
else:
    cumprimento= 'Boa Tarde'

print(saudacao(cumprimento, nome))
print(saudacao)