# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número para calcular seu fatorial: '))
fat = 1
c = n
print(f'Calculando {n}! = ', end='')

while c > 0:
   print(f'{c}', end = '')
   print(f' x ' if c > 1 else ' = ', end='')
   fat = fat * c
   c = c - 1

print(f'{fat}')

"""for lista in range(n, 0, -1):
   print(f'{c}', end='')
   print(f' x ' if c > 1 else ' = ', end='')
   fat = fat * c
   c = c -1
   
print(f'{fat}')"""
