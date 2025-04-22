from random import randint
print(' DESAFIO 068 '.center(45, '='))
print('--' * 20)
print('PAR OU ÍMPAR'.center(35, ' '))
print('--' * 20)
cont = 0

while True:
    ganhou = 0
    jogador = [0, '']

    jogador[0] = int(input('\n > Informe um número: '))

    while jogador[1] != 'P' and jogador[1] != 'I':
        jogador[1] = input(' > Par ou Ímpar [P / I]: ').strip().upper()[0]

    com = randint(0, 10)

    print('\n' + '~~' * 20)
    print(f' * JOGADOR: {jogador[0]}\n * COMPUTADOR: {com}\n * TOTAL: {jogador[0] + com}\n * RESULTADO:', end=' ')
    if (jogador[0] + com) % 2 == 0:
        print('PAR')
        if jogador[1] == 'P':
            ganhou = 1
    else:
        print('ÍMPAR')
        if jogador[1] == 'I':
            ganhou = 1

    print('~~' * 20)
    if ganhou == 1:
        print(' * VOCÊ VENCEU!\n * VAMOS DE NOVO!')
        cont += 1
    else:
        print(f' * GAME OVER!\n * TOTAL DE VITÓRIAS: {cont}')
        break
    print('-=' * 20)
