# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

"""lista = list()

frase = input('Digite a expressão: ')
for dig in frase:
    lista.append(dig)
if lista.count('(') == lista.count(')'):
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')"""

lista = list()

frase = input('Digite a expressão: ')
for dig in frase:
    if dig == '(':
        lista.append(dig)
    elif dig == ')':
        if len(frase) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
