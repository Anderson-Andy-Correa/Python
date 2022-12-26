'''for c in range(1, 10):
    n = int(input('Digite um valor: '))
print('fim')'''

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0 and n != 0:
        par = par + 1
    elif n % 2 != 0:
        impar = impar + 1
print(f'Você digitou {par} valores pares e {impar} valores impares.')