#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#A média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""nomes = []
idades = []
sexos = []
maior = 0
menor = 0

for p in range(1,5):
    print(f'----- {p}ª Pessoa -----')
    nome = input('Nome: ').strip().lower().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F}: ').strip().upper()
    if maior < idade:
        maior = idade
    if sexo == 'F' and idade < 20:
        menor = menor + 1
    nomes.append(f'{nome}')
    idades.append(f'{idade}')
    sexos.append(f'{sexo}')

nome_maior = nomes[idades.index(f'{maior}')]
media = (int((idades[0])) + (int(idades[1])) + (int(idades[2])) + (int(idades[3])))/4

print(f'''A média de idade do grupo é de {media} anos.
O homem mais velho tem {maior} anos e se chama {nome_maior}.
Ao todo são {menor} mulheres com menos de 20 anos.''')"""

soma_idade = 0
media_idade = 0
maior_idade = 0
menores_idade = 0
nome_maior = ''

for pessoa in range(1,5):
    print(f'-----{pessoa}ª PESSOA-----')
    nome = input('Nome: ').strip().lower().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').strip()
    soma_idade = soma_idade + idade
    if maior_idade < idade and sexo in 'Mm':
        maior_idade = idade
        nome_maior = nome
    if idade < 20 and sexo in 'Ff':
        menores_idade = menores_idade + 1

media_idade = soma_idade / 4

print(f'''A média de idade do grupo é de {media_idade} anos.
O homem mais velho tem {maior_idade} anos e se chama {nome_maior}.
Ao todo são {menores_idade} mulheres com menos de 20 anos.''')
