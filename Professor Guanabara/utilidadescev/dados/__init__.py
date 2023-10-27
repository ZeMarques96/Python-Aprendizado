def validador(string):
    while True:
        preco = str(input(string))
        validar = preco.replace(',', '').replace('.', '')
        if validar.isalpha():
            print(f'ERRO: "{preco}" é um preço inválido!')
            continue
        
        elif ',' in preco:
            preco = preco.replace(',', '.')
            preco = float(preco)
            return preco
        
        else:
            print(f'ERRO: "{preco}" é um preço inválido!')
            continue