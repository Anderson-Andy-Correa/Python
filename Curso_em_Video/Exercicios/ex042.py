'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo ', end = '')
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print('\033[33mISÓSCELES\033[m!')
    elif l1 == l2 == l3:
        print('\033[34mEQUILÁTERO\033[m!')
    elif l1 != l2 != l3 != l1:
        print('\033[35mESCALENO\033[m!')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo.')