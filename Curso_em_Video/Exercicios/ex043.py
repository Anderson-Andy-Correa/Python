'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''

weight = float(input('Qual é o seu peso? (Kg) '))
height = float(input('Qual é a sua altura? (m) '))
if weight <= 0 or height <= 0:
    print('\033[31mNúmeros inválidos, tente novamente.\033[m')
else:
    IMC = weight / height ** 2
    print(f'O IMC dessa pessoa é de \033[34m{IMC:.1f}\033[m')
    if 0 < IMC < 18.5:
        print('Você está \033[31mABAIXO DO PESO\033[m normal.')
    elif IMC < 25:
        print('\033[34mPARABÉNS!\033[m, você está na faixa de \033[35mPESO NORMAL\033[m.')
    elif IMC < 30:
        print('Você está em \033[33mSOBREPESO\033[m!')
    elif IMC < 40:
        print('Você está em \033[33mOBESIDADE\033[m!')
    else:
        print('Você está em \033[31mOBESIDADE MÓRBIDA\033[m, cuidado!')
