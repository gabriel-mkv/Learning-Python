print(' DESAFIO 064 '. center(45, '='))
cont = soma = 0
n = int(input('\n - Digite um número (999 para finalizar) -> '))

while n != 999:
    n = int(input('\n - Digite um número (999 para finalizar) -> '))
    soma += n
    cont += 1

print(f'\n * Nº DIGITADOS: {cont}\n * SOMA ENTRE ELES: {soma}')
