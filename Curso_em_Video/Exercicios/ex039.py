#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

#from time import strftime
from datetime import date
s = input('''Qual dos parametrso mais se encaixa na sua situação: 
[ 1 ] Masculino
[ 2 ] Feminino
Sua opção: ''')

if s == "1":
    n = int(input('Ano de nascimento: '))
    #ano = int(strftime('%Y'))
    ano = date.today().year

    print(f'Quem nasceu em {n} tem {ano - n} em {ano}.')
    if (ano - n) < 18:
        print(f'''
    Ainda faltam {n + 18 - ano} para o alistamento.
    Seu alistamtamento será em {n + 18}''')
    elif (ano - n) > 18:
        print(f'''
    Você já deveria ter se alisatado há {ano - n - 18} anos.
    Seu alistamtamento foi em {n + 18}''')
    else:
        print('Você tem que se alisatar IMEDIATAMENTE!')
elif s == "2":
    print('O seu alistamento não é obrigatório.')
else:
    print('Opção inválida! Tente novamente.')