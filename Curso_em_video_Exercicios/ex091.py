#

from time import sleep
from random import randint

print('Valores sorteados:')
dic = dict()
lista = list()

for j in range(1, 5):
    dic['Jogador'] = f'{j}'
    dic['Dado'] = randint(1, 6)
    print(f'    O Jogador {dic["Jogador"]} tirou {dic["Dado"]}')
    sleep(1)
    if j == 1:
        lista.append(dic.copy())
    else:
        for i in lista:
            if dic['Dado'] > i['Dado']:
                lista.insert(lista.index(i), dic.copy())
                break
            if i == lista[-1]:
                lista.append(dic.copy())
                break
print('Ranking dos jogadores:')
for n, maior in enumerate(lista):
    sleep(1)
    print(f'    {n+1}º lugar: Jogador {maior["Jogador"]} com {maior["Dado"]}')
