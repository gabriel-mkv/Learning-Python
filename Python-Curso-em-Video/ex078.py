print(' DESAFIO 078 '.center(45, '=') + '\n')
n = []
mai = []
men = []

for i in range(0, 5):
    n.append(int(input(' > Digite um número: ')))

for p, num in enumerate(n):
    if num == max(n):
        mai.append(p + 1)
    if num == min(n):
        men.append(p + 1)

print('-*' * 20)
print(f' - VALORES INFORMADO -> {n}')
print(f'\n - MAIOR NÚMERO: {mai}º posição - {max(n)}')
print(f' - MENOR NÚMERO: {men}º posição - {min(n)}')
