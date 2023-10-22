pergunta = 'Pergunta'
opcoes = 'Opções'
resposta = 'Resposta'
controle = 0
score = 0
resposta_usuario = ''

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

for controle in range(len(perguntas)):

    for chaves, valores in perguntas[controle].items():
        if chaves == pergunta:
            print(chaves,valores)
        if chaves == opcoes:
            print(f'{chaves}: ')

            for ind, alternativas in enumerate(perguntas[controle][opcoes]):
                print(f'{ind}) {alternativas}')
            resposta_usuario = input('Escolha uma opção: ')
            resposta_usuario = int(resposta_usuario)

            if perguntas[controle][opcoes][resposta_usuario] == perguntas[controle].get(resposta):
                print('Parabéns Você Acertou!!')
                score += 1
                
            else:
                print('Você Errou!')
            print()

print(f'Você acertou {score} de {len(perguntas)} perguntas.')
