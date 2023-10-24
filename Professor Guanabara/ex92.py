import datetime

ano_atual = datetime.datetime.now().year
empregado = {}
empregado['nome'] = str(input('Nome: '))
empregado['nascimento'] = int(input('Ano de nascimento: ')) 
empregado['idade'] = ano_atual - empregado['nascimento']
empregado['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if empregado['ctps'] != 0:
    empregado['contrato'] = int(input('Ano de contratação: '))
    empregado['salario'] = float(input('Salário: '))
    contribuicao = (empregado['contrato'] - ano_atual) * -1
    empregado['aposentadoria'] = (35 - contribuicao) + empregado['idade']

print('-='*30)
for chave, valor in empregado.items():
    print(f'{chave} : {valor}')