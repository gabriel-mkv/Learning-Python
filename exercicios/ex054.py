from datetime import date
maior = []
menor = []
print('\t\t' + ' DESAFIO 54 '.center(45, '=') + '\n')

for c in range(1, 8):
    ano = int(input(f' * Ano de nascimento da {c}º pessoa -> '))

    if (date.today().year - ano) >= 21:
        maior.append(ano)
    else:
        menor.append(ano)

print(f'\n - Há {len(maior)} indivíduos maiores de idade!')
print(f' - E {len(menor)} indivíduos menores de idade!')
