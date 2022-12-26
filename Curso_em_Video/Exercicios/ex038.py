'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais'''
n1 = float(input('\033[33mPrimeiro número\033[m: '))
n2 = float(input('\033[34mSegundo número\033[m: '))
if n1 > n2:
    print(f'O \033[33mPRIMEIRO\033[m valor, (\033[33m{n1:,}\033[m) é maior que (\033[34m{n2:,}\033[m).')
elif n2 > n1:
    print(f'O \033[34mSEGUNDO\033[m valor, (\033[34m{n2:,}\033[m) é maior que (\033[33m{n1:,}\033[m).')
else:
    print(f'Não existe valor maior, os dois, (\033[33m{n1:,}\033[m) e (\033[34m{n2:,}\033[m) são IGUAIS.')