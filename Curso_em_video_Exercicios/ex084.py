# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
cont = nomeMenor = nomeMaior = 0

while True:
    nome = input('Nome: ').strip().capitalize()
    peso = float(input('Peso: '))
    lista.append([nome, peso])
    if len(lista) == 0:
        menor = maior = peso
        nomeMaior = lista[len(lista)][0]
        nomeMenor = lista[len(lista)][0]
    else:
        if maior < peso:
            maior = peso
            nomeMaior = lista[len(lista)][0]
        elif maior == peso:
            nomeMaior = nomeMaior + ', ' + lista[len(lista)][0]
        if menor > peso:
            menor = peso
            nomeMenor = lista[len(lista)][0]
        elif menor == peso:
            nomeMenor = nomeMenor + ', ' + lista[len(lista)][0]
        c = input('Quer continuar? [S/N] ').strip().upper()[0]
    while c not in 'SN':
        c = input('Resposta inválida, tente novamente. Quer continuar? [S/N] ').strip().upper()[0]
    if c in 'N':
        break
print('=-'*30)
print(f'Ao todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de {nomeMaior}')
print(f'O menor peso foi de {menor}Kg. Peso de {nomeMenor}')
