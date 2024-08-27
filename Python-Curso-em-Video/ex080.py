print(' DESAFIO 080 '.center(45, '='))

lista = [int(input('\n > Adicione um valor: '))]
print(' * Valor adicionado ao final da lista!')

for num in range(0, 5):
    n = int(input('\n > Adicione um valor: '))

    for p, item in enumerate(lista):
        if n > item and n > max(lista):
            print(' * Valor adicionado ao final da lista!')
            lista.append(n)
            break
        elif n < item:
            print(f' * Valor adicionado a posição {p + 1} lista!')
            lista.insert(p, n)
            break

print('-*' * 25)
print(f' OS VALORES DIGITADOS EM ORDEM SÃO: {lista}')
