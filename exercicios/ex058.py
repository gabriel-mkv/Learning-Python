from random import randint
user = 11
cont = 0
print('\t\t' + ' DESAFIO 58 '.center(45, '=') + '\n')
print('\033[37m<>-\033[m' * 20)
print('\033[35m Pensei em um número entre 0 e 10, tente adivinhar qual é!\033[m')
print('\033[37m<>-\033[m' * 20)
com = randint(0, 10)

while user != com:
    user = int(input('\n - Digite seu palpite -> '))

    if user > 10 or user < 0:
        print('\n * É entre 0 e 10!')
    else:
        if user > com:
            print(f' - O número é menor que {user}!')
        elif user < com:
            print(f' - O número é maior que {user}!')
        cont += 1

if cont == 1:
    print('\n * ACERTOU DE PRIMEIRA!')
else:
    print(f'\n * PARABÉNS! Com {cont} tentativas você acertou!')
