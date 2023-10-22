perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    }, 
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',   
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
score = 0

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']

    for i,opcao in enumerate(opcoes):
        print(f'{i})',opcao)
        
    print()
    resposta_usuario = input('Escolha uma opção: ')
    
    acertou = False
    resposta_usuario_int = None
    qnt_opcao = len(opcoes)

    if resposta_usuario.isdigit():
        resposta_usuario_int = int(resposta_usuario)
  
    if resposta_usuario_int is not None:
        if resposta_usuario_int >= 0 and resposta_usuario_int < qnt_opcao:
            if opcoes[resposta_usuario_int] == pergunta['Resposta']:
                acertou = True
    if acertou:
        print('Acertou')
        score += 1
    else:
        print('Errou')
    
        
    print()
print(f'Você Acertou {score} de {len(perguntas)} perguntas.')

