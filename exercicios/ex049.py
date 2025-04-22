print('\t\t' + ' DESAFIO 049 '.center(45, '=') + '\n')
n = int(input(' * Informe um número: '))
print('\n\t' + ' TABUADA '.center(30, '-') + '\n')

for c in range(0, 11):
    print(f'{n:2d}  *  {c:2d}  =  {n * c:2d}'.center(35))
