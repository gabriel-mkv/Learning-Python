from emoji import emojize
from time import sleep
from random import randint
lista = [emojize(':moai:'), emojize(':roll_of_paper:'), emojize(':scissors:')]
com = randint(1, 3)
opc = 0

print(f'\t\t{' DESAFIO 045 '.center(45, '-')}\n')
print(emojize('[ 1 ] PEDRA :moai:'))
print(emojize('[ 2 ] PAPEL :roll_of_paper:'))
print(emojize('[ 3 ] TESOURA :scissors:\n'))

while (opc < 1) or (opc > 3):
    opc = int(input(' - FAÇA SUA ESCOLHA -> '))

print('\n JO', end='        ')
sleep(1)
print('KEN', end='        ')
sleep(1)
print('PÔ!\n')
print('-=' * 20)
print(f' * O JOGADOR ESCOLHEU {lista[opc - 1]}!')
print(f' * O COMPUTADOR ESCOLHEU {lista[com - 1]}!')

if opc == com:
    print(' * HOUVE UM EMPATE!')
elif (opc == 1 and com == 3) or (opc == 2 and com == 1) or (opc == 3 and com == 2):
    print(' * VITÓRIA DO JOGADOR!')
else:
    print(' * VITÓRIA DO COMPUTADOR!')

print('-=' * 20)
