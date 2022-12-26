'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''

from time import sleep

escolha = 0
n1 = int(input('\033[34mDigite o primeiro valor: \033[m'))
n2 = int(input('\033[35mDigite o segundo valor: \033[m'))

while escolha != 5:
    print('\033[33m=\033[m' * 30)
    print('''Selecione uma opção:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    print('\033[33m=\033[m' * 30)
    escolha = int(input('Sua escolha: '))
    print('')

    if escolha == 1:
        print(f'A soma entre \033[34m{n1}\033[m e \033[35m{n2}\033[m é \033[36m{n1 + n2}\033[m.')
    elif escolha == 2:
        print(f'A multiplicação entre \033[34m{n1}\033[m e \033[35m{n2}\033[m é \033[36m{n1 * n2}\033[m.')
    elif escolha == 3:
        print(f'Entre \033[34m{n1}\033[m e \033[35m{n2}\033[m o maior termo é \033[36m{max(n1, n2)}\033[m.')
    elif escolha == 4:
        n1 = int(input('\033[34mDigite o primeiro valor: \033[m'))
        n2 = int(input('\033[35mDigite o segundo valor: \033[m'))
    elif escolha == 5:
        print('Saindo do programa...')
    else:
        print('\033[31mOpção inválida, tente novamente.\033[m')
    sleep(1)
print('\033[33m=\033[m' * 30)
print('\033[32mFim do programa! Volte sempre!\033[34m')