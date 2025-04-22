print('====== DESAFIO 034 ======\n')
salario = float(input(' - Informe o salário do funcionário: R$ '))

if salario > 1250:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15

salarioReal = str('%.2f' % salario).replace('.', ',')
aumento = str('%.2f' % aumento).replace('.', ',')
print(f' * O salário de R$ {salarioReal} do funcionário passa ser R$ {aumento}!')
