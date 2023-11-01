def validador(string):
    while True:
        preco = str(input(string)).strip()
        validar = preco.replace(',', '').replace('.', '')
        if validar.isalpha() or validar == '':
            print(f'ERRO: "{preco}" é um preço inválido!')
            continue
        
        else:
            preco = preco.replace(',', '.')
            preco = float(preco)
            return preco
        
