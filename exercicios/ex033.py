print('====== DESAFIO 033 ======\n')
n1 = int(input(' - 1º número: '))
n2 = int(input(' - 2º número: '))
n3 = int(input(' - 3º número: '))
maior = n1
menor = n2

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n3 < n1 and n3 < n2:
    menor = n3

if n1 == n2 or n1 == n3 or n2 == n3:
    if n1 == n2 == n3:
        print(' * Todos os valores são iguais!')
    else:
        print(' * Há dois valores iguais!')
else:
    print(f' * O maior número é {maior}!')
    print(f' * O menor número é {menor}!')
