def conversor(dinheiro):
    return 'R$' + str('%.2f' % dinheiro).replace('.', ',')


print(' DESAFIO 070 '.center(45, '='))
compra = []
inf = [0, 0]
barato = [' ', 0]

while True:
    produto = [' ', 0]
    opc = ' '
    print('\n' + '~~' * 20)
    print('LOJA BALCÃO SEM FUNDO'.center(40, ' '))
    print('~~' * 20)
    produto[0] = input(' > Produto: ').strip().capitalize()
    produto[1] = float(input(' > Valor: R$ ').strip())
    compra.extend([produto])
    print('~~' * 20)
    while opc != 'S' and opc != 'N':
        opc = input(' * Deseja continuar? [S/N] ').strip().upper()
    if opc == 'N':
        print(' FIM DA COMPRA '.center(40, '~'))
        break

for item in compra:
    inf[0] += item[1]
    if item[1] > 1000:
        inf[1] += 1
    if item[1] < barato[1] or barato[1] == 0:
        barato[0] = item[0]
        barato[1] = item[1]

print(f'\nTotal da compra: {conversor(inf[0])}')
print(f'Produtos que custam mais que R$ 1.000,00: {inf[1]}')
print(f'O produto mais barato foi {barato[0]} que custa {conversor(barato[1])}')
