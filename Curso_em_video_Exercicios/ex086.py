# Crie um programa que declare uma matriz de dimensão 3 × 3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

lista = [[], [], []]

for l in range(0, 3):
    for c in range(0, 3):
        lista[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=-'*20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
