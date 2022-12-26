"""teste = []
teste.append('Gustavo')
teste.append(40)
galera = []
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)"""

"""galera = [['João',19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')"""

galera = list()
dado = list()
totmai = totmen = 0

for c in range (0, 3):
    dado.append(str(input('Nome: ')).strip().capitalize())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for pessoa in galera:
    if pessoa[1] >= 21:
        print(f'{pessoa} é maior de idade.')
        totmai += 1
    else:
        print(f'{pessoa[0]} é menor de idade.')
        totmen += 1

print(f'Temos {totmai} maiores e {totmen} menores de idade.')
