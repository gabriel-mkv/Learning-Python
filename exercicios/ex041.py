from datetime import date
print('\t\t====== DESAFIO 041 ======\n')
nascimento = int(input(' - Informe o ano de nascimento do(a) atleta: '))
idade = date.today().year - nascimento
print(f'\n * O(a) atleta tem {idade} anos\033[36m')

if idade <= 9:
    print(' * A SUA CATEGORIA É MIRIM!')
elif idade <= 14:
    print(' * A SUA CATEGORIA É INFANTIL!')
elif idade <= 19:
    print(' * A SUA CATEGORIA É JUNIOR!')
elif idade <= 25:
    print(' * A SUA CATEGORIA É SÊNIOR!')
else:
    print(' * A SUA CATEGORIA É MASTER!')
