print(' DESAFIO 069 '.center(45, '='))
inf = [0, 0, 0]

while True:
    dados = [0, ' ']
    opc = ''
    print('\n' + '~~' * 20)
    print('SEÇÃO DE CADASTRO'.center(40, ' '))
    print('~~' * 20)
    dados[0] = int(input(' > Idade: '))
    while dados[1] != 'M' and dados[1] != 'F':
        dados[1] = input(' > Sexo [M/F]: ').strip().upper()

    if dados[0] >= 18:
        inf[0] += 1
    if dados[1] == 'M':
        inf[1] += 1
    if dados[0] < 20 and dados[1] == 'F':
        inf[2] += 1

    print('~~' * 20)
    while opc != 'S' and opc != 'N':
        opc = input(' * Deseja continuar? [S/N] ').strip().upper()

    if opc == 'N':
        print('~~' * 20)
        break

print(f' * PESSOAS COM MAIS DE 18 ANOS: {inf[0]}')
print(f' * HOMENS CADASTRADOS: {inf[1]}')
print(f' * MULHERES COM MENOS DE 20 ANOS: {inf[2]}')
