#Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser verdadeiras
# Se qualquer valor for considerado falso a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é usado para representar um não valor

entrada = input('[E]ntrar ou [S]air? ')
senha = input('Senha: ')
senha_validacao = '123456'

if entrada == 'E' and senha == senha_validacao:
    print('Logado com Sucesso')
elif entrada == 'E' and senha != senha_validacao:
    print('Senha incorreta')
else:
    print('Você Saiu')
