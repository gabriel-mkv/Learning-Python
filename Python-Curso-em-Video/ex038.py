print('\t\t====== DESAFIO 038 ======\n')
n1 = int(input(' - Informe um número inteiro: '))
n2 = int(input(' - Informe outro número inteiro: '))

if n1 > n2:
    print(f'\033[32m * O número {n1} é maior que o número {n2}!\033[m')
elif n2 > n1:
    print(f'\033[36m * O número {n2} é maior que o número {n1}!\033[m')
else:
    print(f'\033[35m * Os dois números, {n1} e {n2}, são iguais!\033[m')
