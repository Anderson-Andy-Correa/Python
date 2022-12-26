# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('Gerador de PA: ')
print('-='*10)
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = n1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} → ', end = '')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('\nQuantos termos a mais gostaria de saber, caso queira fechar o programa, selecione 0: '))
print(f'Progressão finalizada com {total} termos mostrados.')

