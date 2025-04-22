print('====== DESAFIO 023 ======\n')
num = int(input(' * Digite um número de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'\n - UNIDADE: {u}')
print(f' - DEZENA: {d}')
print(f' - CENTENA: {c}')
print(f' - MILHAR: {m}')

# print('\n - UNIDADE:', num[-1])
# print(' - DEZENA:', num[-2:-1])
# print(' - CENTENA:', num[-3:-2])
# print(' - MILHAR:', num[:-3])
