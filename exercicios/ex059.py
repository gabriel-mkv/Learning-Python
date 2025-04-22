from time import sleep
print('\t\t' + ' DESAFIO 59 '.center(45, '='))
valores = []
opc = 0
menu = '-=' * 20
menu += '\n\t [ 1 ] SOMAR\n\t [ 2 ] MULTIPLICAR\n\t [ 3 ] MAIOR\n\t [ 4 ] NOVOS NÚMEROS'
menu += '\n\t [ 5 ] SAIR DO PROGRAMA\n\n >>> Informe o que deseja: '
valores.append(float(input('\n - 1º número: ')))
valores.append(float(input(' - 2º número: ')))

while opc != 5:
    opc = int(input(menu))

    if opc == 1:
        print(f'\n * A soma entre {valores[0]} + {valores[1]} é {valores[0] + valores[1]}!')
    elif opc == 2:
        print(f'\n * A multiplicação {valores[0]} x {valores[1]} é {valores[0] * valores[1]:.2f}!')
    elif opc == 3:
        print(f'\n * Analisando os números {valores[0]} e {valores[1]},', end=' ')
        if valores[0] == valores[1]:
            print('os valores são iguais!')
        else:
            print(f'o maior valor é {max(valores)}!')
    elif opc == 4:
        print('\n « Informe os valores »')
        valores[0] = float(input('\n - 1º número: '))
        valores[1] = float(input(' - 2º número: '))
    elif opc == 5:
        print('\n * Finalizando o programa...\n' + ('-=' * 20))
        sleep(1)
        print(' * Programa finalizado! Obrigado por usar.')
    else:
        print('\n * Opção inválida, digite novamente!')
