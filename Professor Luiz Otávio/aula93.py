# Try, except, else e finally


try: 
    a = 18
    b = 0
    print('Linha 1')
    c = a / b
    print('Linha 2')

except ZeroDivisionError as error:
    print(error.__class__.__name__, error)
except NameError as error:
    print(error.__class__.__name__, error)
except (TypeError, IndexError) as error:
        print(error.__class__.__name__, error)
except Exception:
    print('ERRO DESCONHECIDO.')
finally:
    print('Chique')