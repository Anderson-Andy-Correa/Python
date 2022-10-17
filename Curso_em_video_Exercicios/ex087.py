# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

lista = [[], [], []]
somaPar = soma3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um valor para [{l}, {c}]: '))
        lista[l].append(n)
        if n % 2 == 0:
            somaPar += n
        if c == 2:
            soma3 += n
print('=-'*20)

for a in range(0, 3):
    for b in range(0, 3):
        print(f'[{lista[a][b]:^5}]', end='')
    print()

print('=-'*20)

print(f'''A soma dos valores pares é {somaPar}.
A soma dos valores da terceira coluna é {soma3}.
O maior valor da segunda linha é {max(lista[1])}.''')
