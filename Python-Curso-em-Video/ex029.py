print('====== DESAFIO 029 ======\n')
vel = int(input(' - Informe a velocidade do veículo: '))

if vel > 80:
    excesso = float((vel - 80) * 7)
    excesso = str('%.2f' % excesso).replace('.', ',')
    print('\033[31m O limite máximo de 80 KM/h foi excedido!')
    print(' Você será MULTADO no valor de \033[m', end='')
    print(f'\033[32mR$ {excesso}!\033[m')
else:
    print('\033[33m Tenha uma boa viagem!\033[m')
