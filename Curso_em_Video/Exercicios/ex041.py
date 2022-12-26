'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''
from datetime import date
ano = date.today().year
yo = int(input('Ano de Nascimento: '))
comp = ano - yo

print(f'O atleta tem \033[32m{comp}\033[m anos. \nClassificação: ', end = '')

if 0 <= comp < 10:
    print('\033[33mMIRIM\033[m.')
elif comp < 15:
    print('\033[34mINFANTIL\033[m.')
elif comp < 20:
    print('\033[35mJÚNIOR\033[m.')
elif comp < 26:
    print('\033[36mSÊNIOR\033[m.')
elif comp > 25:
    print('\033[31mMASTER\033[m.')
else:
    print('\033[31mnúmero inválido, tente novamente.\033[m')