print('\t\t' + ' DESAFIO 051 '.center(45, '=') + '\n')
print('\tPROGRESSÃO ARITMÉTICA: ')
n = int(input('\n - Informe o primeiro termo da progressão: '))
r = int(input(' - Informe a razão da progressão: '))
print('\n * Os 10 primeiros termos dessa progressão são: \n')

for c in range(n, n + (r * 10), r):
    if c < n + (r * 9):
        print(c, end=' -» ')
    else:
        print(c)
