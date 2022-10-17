# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela.

"""lista = list()
menor = 1

for num in range(0, 5):
    valor = int(input('Digite um valor: '))
    if num == 0:
        lista.insert(0, valor)
        print('Adicionado o primeiro termo  da lista...')
    else:
        for teste in lista:
            if valor < teste and menor == num:
                lista.insert(lista.index(teste), valor)
                menor = menor + 1
                print(f'Adicionado na posição {lista.index(valor)} da lista...')
            elif valor >= lista[-1] and menor == num:
                lista.insert(num, valor)
                menor = menor + 1
                print('Adicionado ao final da lista...')
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}.')"""

lista = []

for num in range(0, 5):
    valor = int(input('Digite um valor: '))
    if num == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}.')
