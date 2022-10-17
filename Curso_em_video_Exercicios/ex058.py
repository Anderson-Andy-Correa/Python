#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tries = 0
guess = 11
pc = randint(0, 10)
print("""Sou seu \033[31mcomputador\033[m...
Acabei de pensar em um número entre \033[34m0\033[m e \033[35m10\033[m.
Será que você consegue advinhar qual foi?""")

while guess != pc:
    guess = int(input('Qual é o seu palpite? '))
    while guess > 10:
        guess = int(input('\033[31mValor inválido\033[m, o número tem que estar entre \033[34m0\033[m e \033[35m10\033[m: '))
    tries += 1
    if guess < pc:
        print(f'\033[32mMais\033[m... tente mais uma vez.')
    if guess > pc:
        print(f'\033[33mMenos\033[m... tente mais uma vez.')

print(f'\033[32mParabéns, você venceu!\033[m Só foram necessárias \033[33m{tries}\033[m tentativas.')
