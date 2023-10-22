expression = []
valida = []

expression.append(str(input("Digite sua expressão: ")))
for x in expression:
    for leter in x:
        if leter == '(':
            valida.append(leter)
        elif leter == ')':
            if len(valida) > 0:
                valida.pop()
            else:
                valida.append(leter)
                break
if len(valida) == 0:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')

