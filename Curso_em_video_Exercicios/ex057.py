# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = input('Informe seu sexo: [\033[34mM\033[m/\033[35mF\033[m] ').strip().upper()[0]
while sexo not in 'MmFf':
    sexo = input('Dados inválidos. Por vafor, informe seu sexo: [\033[34mM\033[m/\033[35mF\033[m] ').strip().upper()[0]
if sexo in 'M/m':
    print(f'Sexo \033[34m{sexo}\033[m registrado com sucesso.')
if sexo in 'F/f':
    print(f'Sexo \033[35m{sexo}\033[m registrado com sucesso.')
