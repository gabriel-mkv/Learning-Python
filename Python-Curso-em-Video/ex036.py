print('\t\t====== DESAFIO 036 ======\n')
print('\tBem-vindo a Empréstimos NoFather!\n')
casa = float(input(' - Informe o valor da casa: R$ '))
salario = float(input(' - Informe o seu salário: R$ '))
ano = int(input(' - Informe em quantos anos vai pagar: '))
valorPrest = casa / (ano * 12)
valorMax = salario * 0.3

if valorPrest > valorMax:
    valorMax = str('%.2f' % valorMax).replace('.', ',')
    print('\n\033[31m * Sentimos muito! Seu empréstimo não foi aprovado!\033[m')
    print(f' * Valor máximo da prestação permitido: R$ {valorMax}')
else:
    valorMax = str('%.2f' % valorMax).replace('.', ',')
    print('\n\033[32m * Parábens! Seu empréstimo foi aprovado com sucesso!\033[m')
    print(f' * Valor máximo da prestação permitido: R$ {valorMax}')

salario = str('%.2f' % salario).replace('.', ',')
valorPrest = str('%.2f' % valorPrest).replace('.', ',')
print(f' * Valor da sua prestação: R$ {valorPrest}')
print(f' * Valor do seu salário: R$ {salario}')
