import random

for _ in range(100):
    contador_regressivo_1 = 10
    contador_regressivo_2 = 11
    validador = []
    resultado_digito_1 = 0
    resultado_digito_2 = 0
    cpf_nove_digitos = ''

    for c in range(9):
        cpf_nove_digitos += str(random.randint(0,9))

    for digito in cpf_nove_digitos:
        resultado_digito_1 += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1

    resultado_digito_1 = (resultado_digito_1 * 10) % 11
    digito_1 = resultado_digito_1 if resultado_digito_1 <= 9 else 0
    cpf_dez_digitos = cpf_nove_digitos+ str(digito_1)

    for digito in cpf_dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1

    resultado_digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = resultado_digito_2 if resultado_digito_2 <= 9 else 0 

    cpf_validado  = f'{cpf_nove_digitos}{digito_1}{digito_2}'

    print(cpf_validado)