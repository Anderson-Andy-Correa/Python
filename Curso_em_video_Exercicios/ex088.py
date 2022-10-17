#

from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

vezes = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {vezes} JOGOS ":-^30}')
chute = []

for c in range(0, vezes):
    for n in range(0, 6):
        num = randint(1, 60)
        while num in chute:
            num = randint(1, 60)
        chute.append(num)
    print(f'Jogo {c+1}: {chute}')
    chute.clear()
    sleep(1)
print(f'{f" < BOA SORTE! > ":-^30}')
