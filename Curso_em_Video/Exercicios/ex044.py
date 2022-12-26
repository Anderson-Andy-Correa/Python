'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros'''

print('\033[34m=\033[m'*12, "\033[36mLOJAS ANDY'S\033[m", '\033[34m=\033[m' * 12)
price = float(input("Preço das compras: \033[32mR$\033[m"))
option = int(input('''\033[32mFORMAS DE PAGAMENTO\033[m:
[ \033[34m1\033[m ] à vista no dinheiro ou cheque;
[ \033[35m2\033[m ] à vista no cartão;
[ \033[36m3\033[m ] 2x no cartão;
[ \033[33m4\033[m ] 3x ou mais no cartão.
Qual é a sua opção? '''))
if option == 1:
    print(f'Sua compra de \033[32mR${price:,.2f}\033[m vai custar \033[32mR${price * 0.9:,.2f}\033[m no final.')
elif option == 2:
    print(f'Sua compra de \033[32mR${price:,.2f}\033[m vai custar \033[32mR${price * 0.95:,.2f}\033[m no final.')
elif option == 3:
    print(f'''Sua compra será parcelada em \033[34m2x\033[m de \033[32mR${price/2:,.2f} \033[33mSEM JUROS\033[m
Sua compra vai custar \033[32mR${price:,.2f}\033[m no final.''')
elif option == 4:
    taxes = int(input('Quantas parcelas? '))
    print(f'''Sua compra será parcelada em \033[34m{taxes}x\033[m de \033[32mR${price*1.2/taxes:,.2f} \033[31mCOM JUROS\033[m
Sua compra de \033[33mR${price:,.2f}\033[m vai custar \033[32mR${price * 1.2:,.2f}\033[m no final, com um juros de \033[31mR${price * 0.2:,.2f}\033[34m.''')
else:
    print(f'\033[31mOpção inválida de pagamento, tente novamente!\033[m')
