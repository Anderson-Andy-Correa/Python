#

teste = ''
n = s = c = 0
menor = maior = 0

while teste != 'N':
    n = int(input('Digite um número: '))
    if menor == 0 == menor:
        menor = n
        maior = n
    if menor > n:
        menor = n
    if maior < n:
        maior = n
    s += n
    c += 1
    teste = input('Deseja continuar digitando? Y/N ').strip().upper()
    if teste not in 'YyNn':
        print('Opção inválida, tente novamente.')
        teste = input('Deseja continuar digitando? Y/N ').strip().upper()
print(f'''A média dos valores solicitados foi de {s/c}
O maior número foi {menor}
E o Maior número foi {maior}''')