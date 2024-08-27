print('\t\t' + ' DESAFIO 062 '.center(45, '=') + '\n')
print('\tSUPER PROGRESSÃO ARITMÉTICA: ')
n = int(input('\n - Informe o primeiro termo da progressão: '))
r = int(input(' - Informe a razão da progressão: '))
cont = qtd = 1
termo = 10
print('\n * Os 10 primeiros termos dessa progressão são: \n')

while qtd != 0:

    if cont <= 10:
        print(n, end='')
        print(' -» ' if cont < 10 else ' -» PAUSA', end='')
        n += r
        cont += 1
    else:
        qtd = int(input('\n\n - Quantos termos deseja imprimir a mais? '))
        termo += qtd
        for c in range(0, qtd):
            print(n, end='')
            print(' -» ' if c < (qtd - 1) else ' -» PAUSA', end='')
            n += r

print(f'\n * Programa finalizado com {termo} termos imprimidos!')
