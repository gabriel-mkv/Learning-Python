valores = []
# menor = 0
# maior = 0
print('\t\t' + ' DESAFIO 55 '.center(45, '=') + '\n')

for c in range(1, 6):
    peso = float(input(f' - Informe o peso da {c}º pessoa: '))

#    if c == 1:
#        menor = peso
#        maior = peso
#    else:
#        if peso > maior:
#           maior = peso
#        if peso < menor:
#            menor = peso

    valores.append(peso)
    valores.sort()

print(f'\n * O maior peso foi {valores[-1]:.1f} KG!')
print(f' * O menor peso foi {valores[0]:.1f} KG!')
