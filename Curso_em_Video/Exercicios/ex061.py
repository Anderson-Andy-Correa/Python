# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA.
# Mostre os 10 primeiros termos da progressão usando a estrutura while.

print('Gerador de PA')
print('-='*10)
n1 = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termos = 0

while termos != 10:
    termos = termos + 1
    if termos == 1:
        n1 = n1
        print(f'{n1} → ', end='')
    else:
        n1 = n1 + razão
        print(f'{n1} → ', end='')
print('Fim')

"""n1 = int(input('Primeiro termo: '))
razão = int(input('Razão: '))

for c in range(n1, (n1 + razão * 10), razão):
    if c == razão:
        n1 = n1
        print(f'{n1} → ', end='')
    else:
        n1 = n1 + razão
        print(f'{n1} → ', end='')
print('Fim')"""
