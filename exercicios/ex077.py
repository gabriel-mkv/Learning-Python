print(' DESAFIO 077 '.center(45, '='))

words = ('jogar', 'expulsar', 'adorar', 'receba', 'paralelepipedo', 'joaninha',
         'arrombar', 'exercer', 'machucado', 'lambida', 'olhos', 'pedreiro')

for item in words:
    print(f'\n> A palavra {item.upper()} possui as vogais: ', end='')
    for letra in item:
        if letra in 'aeiou':
            print(letra, end=' ')
