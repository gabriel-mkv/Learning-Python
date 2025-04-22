print('\t\t' + ' DESAFIO 53 '.center(45, '=') + '\n')
frase = input(' * Informe uma frase -> ').upper().replace(' ', '')
print(f' * Frase informada: {frase}\n * Inverso da frase: {frase[::-1]}')

if frase[::-1] == frase:
    print(' * A frase é um PALÍNDROMO!')
else:
    print(' * A frase NÃO é um PALÍNDROMO!')
