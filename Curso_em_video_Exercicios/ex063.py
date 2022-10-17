# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-' * 30)
print('{:^30}'.format("Sequencia de Fobonacci"))
print('-' * 30)
n = int(input('Quantos termos você que mostrar?: '))
inicio = 0
passo1 = 1
passo2 = 0
bonito = n
print('~' * (4 * bonito))
while n != 0:
    print(f'{inicio} → ', end='')
    passo2 = passo1
    passo1 = inicio
    inicio = passo1 + passo2
    n = n - 1
print('Fim')
print('~' * (4 * bonito))
