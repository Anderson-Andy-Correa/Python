#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

resultado = ''
while resultado != 'Vitória!':

      print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

      player = int(input('Qual é a sua jogada? '))
      if player in (0, 1, 2):
            pc = randint(0, 2)
            op = ['PEDRA', 'PAPEL', 'TESOURA']

            print('JO')
            sleep(1)
            print('KEN')
            sleep(1)
            print('PO!!!')

            print('-=' * 20)
            print(f'''Sua escolha foi {op[player]}
A escolha do Computador foi {op[pc]}''')
            print('-=' * 20)

            win = 'vitória!'
            lose = 'Derrota!'
            tie = 'Empate!'

            if player == pc:
                  resultado = 'Empate'
                  print(resultado)
            elif player == 0 and pc == 2:
                  resultado = 'Vitória!'
                  print(resultado)
            elif player == 1 and pc == 0:
                  resultado = 'Vitória!'
                  print(resultado)
            elif player == 2 and pc == 1:
                  resultado = 'Vitória!'
                  print(resultado)
            else:
                  resultado = 'Derrota'
                  print(resultado)
      else:
            print('Opção inválida, tente novamente.')
            resultado = 'Inválido'