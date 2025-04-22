from random import randrange
from time import sleep
print('====== DESAFIO 028 ======\n')
n = int(randrange(0, 5))
print('\033[37m<>-\033[m' * 20)
print('\033[35m Pensei em um número entre 0 e 5, tente adivinhar qual é!\033[m')
print('\033[37m<>-\033[m' * 20 + '\n')
opc = int(input(' - Digite o número: '))
print('   ANALISANDO...')
sleep(3)

if (opc >= 0) and (opc <= 5):
    if opc == n:
        print('\n * Parábens, você acertou o número!')
    else:
        print('\n * Você errou!')
        print(f' * O número era {n}!')
else:
    print(' * Escolha um número válido!')
