print(' DESAFIO 079 '.center(45, '='))

num = [int(input('\n > Informe um número: '))]
print(' Valor adicionado!')

while True:
    n = int(input('\n > Informe um número: '))

    for p in num:
        if n == p:
            print(' * Valor repetido não adicionado!')
            break
    else:
        print(' * Valor adicionado!')
        num.append(n)

    opc = input(' - Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break

print(f' - Valores digitados: {sorted(num)}')
