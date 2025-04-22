print(' DESAFIO 071 '.center(45, '='))
'cedulas = [0, 0, 0, 0]'
cedulas = 50
total = 0
print('\n' + '~~' * 20)
print('BANCO RECEBA!'.center(40, ' '))
print('~~' * 20)
valor = int(input(' > Valor que deseja sacar: R$ '))

while True:
    '''if valor >= 50:
        cedulas[0] = valor // 50
        valor = valor - (cedulas[0] * 50)
        print(f'\nTotal de notas de R$ 50: {cedulas[0]}')
    if valor >= 20:
        cedulas[1] = valor // 20
        valor = valor - (cedulas[1] * 20)
        print(f'Total de notas de R$ 20: {cedulas[1]}')
    if valor >= 10:
        cedulas[2] = valor // 10
        valor = valor - (cedulas[2] * 10)
        print(f'Total de notas de R$ 10: {cedulas[2]}')
    if valor != 0:
        cedulas[3] = valor * 1
        valor = valor - (cedulas[3] * 1)
        print(f'Total de notas de R$ 1: {cedulas[3]}')
    break'''

    if valor >= cedulas:
        valor -= cedulas
        total += 1
    else:
        if total > 0:
            print(f'Total de notas de R$ {cedulas}: {total}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        elif valor == 0:
            break
        total = 0

print('~~' * 20)
print('RECEBA O DINHEIRO!')
