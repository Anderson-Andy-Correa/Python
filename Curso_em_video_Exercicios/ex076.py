# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print('-'*40)
print('{:^40}'.format('LISTA DE PREÇOS'))
print('-'*40)

tupla = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 15.9,
         'Estojo', 25,
         'Transferidor', 4.2,
         'Compasso', 9.99,
         'Mochila', 120.32,
         'Canetas', 22.3,
         'Livro', 34.9)

for pos, lista in enumerate(tupla):
    if pos % 2 == 0:
        print(f'{lista:.<30}', end='')
    else:
        print(f'R$ {lista:>6.2f}')
print('-'*40)
