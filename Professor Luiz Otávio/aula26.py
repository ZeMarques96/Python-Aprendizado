"""
Formatação básica de strings
s - string
d - int
f - float
.< número de dígitos >f
x ou X - Hexadecimal
(Caractere (><^) (Quantidade))
> - Esquerda
< - Direita
^ - Centro 
Sinal - ou + ou -
Ex. : 0>-100, .1f
Conversion flags - !r !s !a __repr__ __str__"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{-1000.45686456:+,.3f}')
print(f'O hexadecimal de 1500 é {1500:08x}')
