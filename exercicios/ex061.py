print('\t\t' + ' DESAFIO 061 '.center(45, '=') + '\n')
print('\tPROGRESSÃO ARITMÉTICA: ')
n = int(input('\n - Informe o primeiro termo da progressão: '))
r = int(input(' - Informe a razão da progressão: '))
cont = 1
print('\n * Os 10 primeiros termos dessa progressão são: \n')

while cont <= 10:
    print(n, end='')
    print(' -» ' if cont < 10 else ' -» FIM', end='')
    cont += 1
    n += r
