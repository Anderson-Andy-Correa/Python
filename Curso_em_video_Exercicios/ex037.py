n = int(input('Digite um número inteiro: '))
c = int(input('''Ecolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))
if c == 1:
    print(f'{n} convertido para BINÁRIO é igual a {bin(n).replace("0b", "")}')
elif c == 2:
    print(f'{n} convertido para OCTAL é igual a {oct(n).replace("0o", "")}')
elif c == 3:
    print(f'{n} convertido para HEXADECIMAL é igual a {hex(n).replace("0x", "")}')
else:
    print(f'Desculpe, mas o número {c} não corresponde uma opção válida. Tente novamente.')
