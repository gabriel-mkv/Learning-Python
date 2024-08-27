print('\t\t' + ' DESAFIO 57 '.center(45, '=') + '\n')
sexo = (input(' - Informe seu sexo [M / F]: ').upper().strip())

while (sexo != 'M') and (sexo != 'F'):
    sexo = (input(' - Por favor, digite um valor válido [M / F]: ').upper().strip())

print(f'\n * O sexo {sexo} foi registrado!')
