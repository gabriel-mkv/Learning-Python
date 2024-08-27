print(' DESAFIO 076 '.center(45, '='))

cont = 0
itens = ('Bola', 13.25, 'Lego', 45.00, 'Carrinho', 14.60, 'Amoeba', 10.00, 'Boneco', 24.55)

print('\n' + '--' * 20)
print('TOPA-TUDO RECEBA'.center(40))
print('--' * 20)
for i in range(0, len(itens)):
    if i % 2 == 0:
        print(f'{itens[i]:.<32}', end='')
    else:
        print(f'R$ {itens[i]:.2f}')
print('--' * 20)