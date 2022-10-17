#

from time import sleep

lista = []
cont = 0

while True:
    aluno = input('Nome: ').strip().capitalize()
    n1 = float(input('Nota 1: '))
    if n1 < 0 or n1 > 10:
        while n1 < 0 or n1 > 10:
            n1 = float(input('Nota inválida, a nota deve estar entre 0 e 10. '
                             '\nNota 1: '))
    n2 = float(input('Nota 2: '))
    if n2 < 0 or n2 > 10:
        while n2 < 0 or n2 > 10:
            n2 = float(input('Nota inválida, a nota deve estar entre 0 e 10. '
                             '\nNota 1: '))
    media = (n1 + n2)/2
    lista.append([aluno, [n1, n2], media])
    cont += 1
    continua = input('Quer continuar? [S/N]').strip().upper()[0]
    while continua not in 'SN':
        continua = input(
            '\033[31mResposta inválida, tente novamente.\033[m '
            '\nQuer continuar? [S/N] ').strip().upper()[0]
    if continua in 'N':
        break
print('\033[37m-\033[m'*30)
print(f'\033[32m{"No.":<5}\033[m', end='')
print(f'\033[34m{"NOME":<15}\033[m', end='')
print(f'\033[35m{"MÉDIA":>5}\033[m')
print('\033[37m-\033[m'*30)
for c in range(0, cont):
    print(f'\033[32m{f"{c}":<5}\033[m', end='')
    print(f'\033[34m{f"{lista[c][0]}":<15}\033[m', end='')
    if float(f"{lista[c][2]}") >= 6:
        print(f'\033[35m{float(f"{lista[c][2]}"):>5.1f}\033[m')
    else:
        print(f'\033[31m{float(f"{lista[c][2]}"):>5.1f}\033[m')
print('\033[37m-\033[m'*30)

while True:
    if cont == 1:
        show = int(input(f'Mostrar notas de qual aluno? '
                         f'\n\033[32m[Apenas número {cont-1} válido] \033[m'
                         f'\n\033[36m(999 interrompe): \033[m'))
    elif cont == 2:
        show = int(input(f'Mostrar notas de qual aluno? '
                         f'\n\033[32m[Ver no índice os correspondentes, números 0 ou {cont-1} válidos] \033[m'
                         f'\033[36m\n(999 interrompe): \033[m'))
    else:
        show = int(input(f'Mostrar notas de qual aluno? '
                         f'\033[32m\n[Ver no índice os correspondentes, números entre 0 e {cont-1} válidos] \033[m'
                         f'\033[36m\n(999 interrompe): \033[m'))
    if show == 999:
        break
    if 0 <= show < cont:
        print(f'Notas de \033[34m{lista[show][0]}\033[m são ', end='')
        if lista[show][1][0] >= 6:
            print(f'\033[33m{lista[show][1][0]}\033[m ', end='')
        else:
            print(f'\033[31m{lista[show][1][0]}\033[m ', end='')
        print('e ', end='')
        if lista[show][1][1] >= 6:
            print(f'\033[33m{lista[show][1][1]}\033[m.')
        else:
            print(f'\033[31m{lista[show][1][1]}\033[m.')
    else:
        print('\033[31mOpção inválida, tente novamente.\033[m')
    print('\033[37m-\033[m' * 30)
print('\033[37m-\033[m' * 30)
print('\033[33mFINALIZANDO...\033[m')
sleep(1)
print('\033[32m<<< VOLTE SEMPRE! >>>\033[m')
