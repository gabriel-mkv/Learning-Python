print(' DESAFIO 067 '.center(45, '=') + '\n')

while True:
    num = int(input(' > Qual tabuada deseja ver? '))
    print('~~' * 22)
    if num < 0:
        print(' - TABUADA ENCERRADA, ATÉ A PRÓXIMA!')
        break
    for c in range(1, 11):
        print(f'{num:>16} * {c} = {num * c}')
    print('~~' * 22)
