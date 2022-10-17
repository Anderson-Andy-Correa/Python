# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = input('Quer continuar? [S/N}').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('Valor inválido. Quer continuar? [S/N}').strip().lower()[0]
    if continuar in 'N':
        break
print('-='*20)
lista.sort()
print(f'Você digitou os valores {lista}')
