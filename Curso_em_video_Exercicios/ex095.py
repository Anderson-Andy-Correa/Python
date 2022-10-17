#

tot = 0
dic = dict()
lista = list()
listaF = list()

while True:
    dic['nome'] = input('Nome: ').strip().capitalize()
    partidas = int(input(f'Quantas partidas {dic["nome"]} jogou? '))
    for g in range(0, partidas):
        lista.append(int(input(f'Quantos gols na partida {g}? ')))
        tot += lista[g]
    dic['gols'] = lista[:]
    dic['total'] = tot
    listaF.append(dic.copy())
    lista.clear()
    tot = 0
    r = input('Quer continuar? [S/N] ').strip().upper()[0]
    while r not in 'SN':
        r = input('Inserção inválida, tente novamente. \nQuer continuar? [S/N] ').strip().upper()[0]
    if r == 'N':
        break
    print('-' * 30)
print('-='*30)
print(f'{"cod":<5}{"nome":<15}{"gols":<15}{"total":<5}')
print('-'*40)
for n, i in enumerate(listaF):
    for v in i.values():
        print(f'{n:^5}{i["nome"]:<15}{str(i["gols"]):<15}{i["total"]:<5}')
        break
print('-'*40)
while True:
    show = int(input('Mostrar dados de qual jogador? [999 para encerrrar] '))
    if show == 999:
        break
    if show >= len(listaF) or 0 > show:
        print(f'ERRO! Não existe jogador com código {show}! Tente novamente.')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {listaF[show]["nome"]}:')
        for n, i in enumerate(listaF[show]["gols"]):
            print(f'No jogo {n} fez {i} gols.')
    print('-' * 40)
print("<< VOLTE SEMPRE >>")
