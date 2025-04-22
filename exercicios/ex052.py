print('\t\t' + ' DESAFIO 052 '.center(45, '=') + '\n')
num = int(input(' - Informe um número: '))
cont = 0

for c in range(1, num + 1):

    if num % c == 0:
        print('\033[34m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')

    print(c, end=' ')

if cont == 2:
    print(f'\n\n\033[m O número {num} é divisível por {cont} números, ele É PRIMO!')
else:
    print(f'\n\n\033[m O número {num} é divisível por {cont} números, ele NÃO É PRIMO!')
