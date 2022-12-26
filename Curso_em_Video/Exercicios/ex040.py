'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'Tirando \033[35m{n1}\033[m e \033[36m{n2}\033[m a média do aluno é \033[34m{m:.1f}\033[m')

if m > 7 and m < 10:
    print('O aluno está \033[32mAPROVADO\033[m.')

elif 5 <= m < 7:
    print('O aluno está de \033[33mRECUPERAÇÂO\033[m.')

elif m < 5:
    print('O aluno está \033[31mREPROVADO\033[m')
else:
    print('Opção inválida! Tente novamente.')