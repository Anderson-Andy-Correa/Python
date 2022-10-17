# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

tupla = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número: ')),
         int(input('Digite o último número: ')))
cont = 0
pos3 = ''

print('Você digitou os valores: ', end='')

for pos, lista in enumerate(tupla):
    if lista == 9:
        cont += 1
    if lista == 3 and pos3 == '':
        pos3 = pos
    if pos == 2:
        print(lista, end= ' e ')
    elif pos == 3:
        print(f'{lista}.')
    else:
        print(lista, end=', ')

if cont == 0:
    print('O valor 9 não apareceu nenhuma vez.')
elif cont == 1:
    print(f'O valor 9 apareceu {cont} única vez.')
else:
    print(f'O valor 9 apareceu {cont} vezes.')
if pos3 == '':
    print(f'O valor 3 não foi digitado.')
else:
    print(f'O valor 3 apareceu na {pos3+1}ª posição.')

#if
print('Os valores pares digitados foram: ', end='')

for pos, lista in enumerate(tupla):
    if lista % 2 == 0:
            print(lista, end=' ')
