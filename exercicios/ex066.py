print(' DESAFIO 066 '.center(45, '='))
s = c = 0

while True:
    n = int(input('\n > Digite um número: '))
    if n == 999:
        break
    s += n
    c += 1

print(f'\n - Nº DIGITADOS: {c}\n - SOMA TOTAL: {s}')
