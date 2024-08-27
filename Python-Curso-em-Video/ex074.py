from random import randint

print(' DESAFIO 074 '.center(45, '='))

n = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'\n > OS VALORES SORTEADOS FORAM: {n}')
print(f' > MAIOR VALOR: {max(n)}')
print(f' > MENOR VALOR: {min(n)}')
