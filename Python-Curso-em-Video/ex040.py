print('\t\t====== DESAFIO 040 ======\n')
n1 = float(input(' - Informe a 1º nota: '))
n2 = float(input(' - Informe a 2º nota: '))
media = (n1 + n2) / 2
print(f'\n * A média do aluno foi {media:.2f}!')

if media < 5:
    print('\033[31m * O ALUNO FOI REPROVADO!\033[m')
elif 6.9 >= media >= 5:
    print('\033[33m * O ALUNO ESTÁ EM RECUPERAÇÃO!\033[m')
else:
    print('\033[32m * O ALUNO FOI APROVADO!\033[m')
