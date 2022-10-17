# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
menor = 0
maior = 0

print("Os números sorteados foram: ", end='')
for pos, lista in enumerate(tupla):
    if pos == 0:
        menor = lista
        maior = lista
    else:
        if menor > lista:
            menor = lista
        if maior < lista:
            maior = lista
    if pos == 3:
        print(lista, end=' e ')
    elif 0 <= pos <= 2:
        print(lista, end=', ')
    else:
        print(f'{lista}.')
print(f'''O maior valor sorteado foi {maior}.
O menor valor sorteado foi {menor}.''')
