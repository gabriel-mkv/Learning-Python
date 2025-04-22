print('\t\t====== DESAFIO 043 ======\n')
print('\t « CÁLCULO IMC »\n')
sexo = input(''' [M] - Masculino
 [F] - Feminino\n
 - Informe o sexo: ''').upper()

if (sexo != 'M') and (sexo != 'F'):
    print(' * Valor inválido!')
    exit()

peso = float(input(' - Informe o peso (em KG): '))
altura = float(input(' - Informe a altura (em metros): '))
imc = peso / altura ** 2
print(f'\n * O IMC desse indivíduo é {imc:.1f}\033[31m')

if imc < 18.5:
    print(' * ABAIXO DO PESO')
elif 25 > imc >= 18.5:
    print('\033[32m * PESO IDEAL')
elif 30 > imc >= 25:
    print('\033[33m * SOBREPESO')
elif 40 > imc >= 30:
    print(' * OBESIDADE')
else:
    print(' * OBESIDADE MÓRBIDA')
