lista = []

for c in range(0, 3):
    nome = input('Nome: ')
    n1 = int(input('Nota 1: '))
    n2 = int(input('Nota 2: '))
    media = (n1 + n2)/2
    lista.append([nome, [n1, n2], media])
print(lista)
