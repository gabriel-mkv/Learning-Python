print('\t\t' + ' DESAFIO 60 '.center(45, '='))
print('\n\t---- FATORIAL ----')
n = int(input(' - Informe um número para calcular seu fatorial: '))
c = n
resultado = 1
print(f'\n{n}! =', end=' ')

if n == 0:
    print('1')

while c >= 1:
    resultado *= c
    print(f'{c}', end=' ')
    print(f'x ' if c > 1 else f'= {resultado}', end='')
    c -= 1

'''
for i in range(n, 0, -1):
    resultado = resultado * i
    print(f'{i}', end=' ')

    if i > 1:
        print('x ', end='')
    elif i == 1:
        print(f'= {resultado}')
'''