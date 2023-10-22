"""

CPR: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores
 por uma contagem regressiva começando de 10

746.824.890-70
    10  9   8   7   6   5   4   3   2
*   7   4   6   8   2   4   8   9   0
    70  36  48  56  12  20  32  27  0
 
 Somar todos os resultados: 
 70+36+48+56+12+20+32+27+0 = 301
 Multiplicar o resultado anterior por 10
 301 * 10 = 3010
 Obter o resto da divisão da conta anterior por 11
 3010 % 11 = 7
 Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O primeiro dígito do CPF é 7"""

#cpf = '184.028.000-09'
import re
cpf = '064.418.489-29'
#cpf = input('Digite seu CPF aqui: ')
contador_regressivo_1 = 10
contador_regressivo_2 = 11
validador = []
resultado_digito_1 = 0
resultado_digito_2 = 0

validando_entrada_cpf = cpf == cpf[0] * len(cpf)

cpf_formatado = re.sub(r'[^0-9]','', cpf)
cpf_nove_digitos = cpf_formatado[:9]

for digito in cpf_nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

resultado_digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = resultado_digito_1 if resultado_digito_1 <= 9 else 0
cpf_dez_digitos = cpf_formatado[:9]+ str(digito_1)

for digito in cpf_dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

resultado_digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = resultado_digito_2 if resultado_digito_2 <= 9 else 0 
cpf_validado  = f'{cpf_nove_digitos}{resultado_digito_1}{resultado_digito_2}'
if cpf_formatado == cpf_validado:
    print(f'O CPF {cpf} É VÁLIDO')
else:
    print(f'O CPF {cpf} NÃO É UM CPF VÁLIDO!')
