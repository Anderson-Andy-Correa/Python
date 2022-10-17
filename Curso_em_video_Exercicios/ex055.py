#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for pess in range(1,6):
    peso = float(input(f'Peso da {pess}ª pessoa: '))
    if pess == 1:
        menor = peso
        maior == peso
    else:
        if maior < peso:
            maior = peso
        if menor > peso and peso != 0:
            menor = peso

print(f'O maior peso lido foi de {maior}Kg \nO menor peso lido foi de {menor}Kg')
