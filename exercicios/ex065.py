print(' DESAFIO 065 '.center(45, '='))
opc = ''
cont = 0
valores = [0, 0, 0]

while opc.upper() != 'N':
    n = int(input('\n > Informe um número: '))
    valores[0] += n

    if n > valores[1]:
        valores[1] = n
    if n < valores[2] or cont == 0:
        valores[2] = n
    cont += 1
    opc = input(' > Continuar [S / N]? ').strip()[0]

print(f'\n * Nº DIGITADOS: {cont}\n * MÉDIA: {valores[0] / cont:.2f}')
print(f' * MAIOR: {valores[1]}\n * MENOR: {valores[2]}')
