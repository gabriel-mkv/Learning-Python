print(' DESAFIO 075 '.center(45, '=') + '\n')
n = []
condicao = [0, 0]

# n = (int(input(' > Digite um número: ')),
#     (int(input(' > Digite outro número: ')),
#     (int(input(' > Digite mais um número: ')),
#     (int(input(' > Digite o último número: ')))

for i in range(0, 4):
    n.append(int(input(' > Digite um número: ')))
    if n[i] == 9:
        condicao[0] += 1
    if n[i] == 3:
        condicao[1] += 1

tupla = (n[0], n[1], n[2], n[3])

# n.count(9)
print(f' > O valor 9 apareceu {condicao[0]} vezes!')
if condicao[1] == 0:
    print(' > O valor 3 não apareceu em nenhuma posição!')
else:
    print(f' > O valor 3 apareceu na posição {tupla.index(3) + 1}!')
print(f' > Números pares digitados: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')
