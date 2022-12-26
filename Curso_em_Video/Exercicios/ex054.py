# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
novo = 0
velho = 0

for num in range(1,8):
    n = int(input(f'Em que ano a {num}ª pessoa nasceu? '))
    if (atual - n) >= 21:
        velho = velho + 1
    elif (atual - n) < 21:
        novo = novo + 1
if velho == 0:
    print(f'Não tivemos pessoas maiores de idade.')
elif velho == 1:
    print(f'Ao todo tivemos {velho} pessoa maior de idade.')
elif velho > 1:
    print(f'Ao todo tivemos {velho} pessoas maiores de idade.')
if novo == 0:
    print(f'E não tivemos pessoas menores de idade.')
elif novo == 1:
    print(f'E também tivemos {novo} pessoa menor de idade.')
elif novo > 1:
    print(f'E também tivemos {novo} pessoas menores de idade.')
