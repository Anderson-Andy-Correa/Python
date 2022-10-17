# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = cont = soma = 0

while True:
    print('-'*30)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    while True:
        if cont == 10:
            break
        cont += 1
        soma += n
        print(f'{n} x {cont:2} = {soma}')
    soma = 0
    cont = 0
print('PROGRAMA DE TABUADA ENCERRADO. Volte sempre!')