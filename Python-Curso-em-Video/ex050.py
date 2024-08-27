print('\t\t' + ' DESAFIO 050 '.center(45, '=') + '\n')
i = 0
p = 0

for c in range(1, 7):
    n = int(input(f' - Informe o {c}º número -> '))
    if n % 2 == 0:
        p += n
    else:
        i += n

print(f'\n * A soma dos número pares digitados é {p}!')
print(f'\n * A soma dos número ímpares digitados é {i}!')
