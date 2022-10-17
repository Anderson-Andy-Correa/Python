# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla = ('APRENDER', 'PROGRAMA', 'LINGUAGEM', 'PYTHON', 'CURSO',
         'GRÁTIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
         'PROGRAMADOR', 'FUTURO')

for lista in tupla:
    print(f'Na palavra {lista.upper()} temos ', end='')
    for pos, letra in enumerate(lista):
        if letra.upper() in 'AÁÃÂÀEÉÊIÍOÔÕUÚÛ':
            print(letra.lower(), end=' ')
        if pos == len(lista)-1:
            print('')