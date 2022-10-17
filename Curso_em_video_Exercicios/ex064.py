#

n = 0
cont = 0
soma = n
while n != 999:
    n = int(input('Digite um número. Digite "999" para sair: '))
    if n != 999:
        cont += 1
        soma += n
print(f'''A soma de todos os {cont} valores é {soma}.

Saindo do programa...''')