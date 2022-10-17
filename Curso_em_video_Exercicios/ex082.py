# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = list()
par = list()
ímpar = list()

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    continuar = input('Quer continuar? [S/N} ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Opção inválida, tente novamente. QUer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break
lista.sort()
for item in lista:
    if item % 2 == 0:
        par.append(item)
    else:
        ímpar.append(item)
print('-='*30)
print(f'''A lista completa é {lista}
A lista de pares é {par}
A lista de Impares é {ímpar}''')
