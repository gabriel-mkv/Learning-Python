nome = []
idade = []
sexo = ['', '', '', '']
velhoEqtdmulher = ['', 0, 0]
print('\t\t' + ' DESAFIO 56 '.center(45, '='))

for c in range(0, 4):
    print('\n' + f' {c + 1}º INDIVÍDUO '.center(26, '-'))
    nome.append(input(' - NOME: ').upper().strip())
    idade.append(int(input(' - IDADE: ')))

    while True:
        sexo[c] = (input(' - SEXO [M / F]: ').upper())
        if sexo[c] == 'M' or sexo[c] == 'F':
            break

    if (idade[c] < 20) and (sexo[c] == 'F'):
        velhoEqtdmulher[2] += 1

    if (velhoEqtdmulher[1] == 0) and (sexo[c] == 'M'):
        velhoEqtdmulher[0] = nome[c]
        velhoEqtdmulher[1] = idade[c]
    else:
        if (idade[c] > velhoEqtdmulher[1]) and (sexo[c] == 'M'):
            velhoEqtdmulher[0] = nome[c]
            velhoEqtdmulher[1] = idade[c]

print(f'\n * Média de idade do grupo: {sum(idade) / 4:.1f} anos')
print(f' * O homem mais velho é {velhoEqtdmulher[0]} e tem {velhoEqtdmulher[1]} anos')
print(f' * São {velhoEqtdmulher[2]} mulheres com menos de 20 anos')
