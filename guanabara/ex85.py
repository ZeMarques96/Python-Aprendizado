lista = [5, 8, 2, 4, 3, 7, 10]
# lista = [
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
#     int(input('Digite um valor:')),
# ]
lista_impar = [ impar 
               for impar in lista
               if impar % 2 == 1
               ]
lista_par = [
    par 
    for par in lista
    if par % 2 == 0
]
lista_final = []
lista_final.append(lista_impar)
lista_final.append(lista_par)
print(lista_final)
print(f'Os valores pares digitados foram: ', sorted(lista_par))
print(f'Os valores impares digitados foram: ', sorted(lista_impar))