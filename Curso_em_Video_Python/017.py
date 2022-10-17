"""lista = [2, 5, 9, 1]
lista[2] = 3
lista.append(7)
lista.sort(reverse=True)
lista.insert(2, 2)
lista.remove(2) #Só o primiro da lista
lista.remove(5) if 5 in lista else print('Não achei o número 5')
#lista.pop(2)
print(lista)
print(f'Essa lsita tem {len(lista)} elementos.')"""

"""valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))

for pos, valor in enumerate(valores):
    print(f'Na posição {pos}, encontrei o valor {valor}!')
print('Cheguei ao final da lista.')"""

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8

print(f'Lista A: {a}')
print(f'Lista B: {b}')
