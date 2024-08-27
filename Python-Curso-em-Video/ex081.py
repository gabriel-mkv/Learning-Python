print(' DESAFIO 081 '.center(45, '='))
lista = []

while True:
    lista.append(int(input('\n > Informe um valor: ')))
    opc = input(' - Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break

print('-*' * 25)
print(f' - A quantidade de valores digitados foram {len(lista)}!')
print(f' - Valores em ordem decrescente: {sorted(lista, reverse=True)}')
for p, i in enumerate(lista):
    if i == 5:
        print(f' - O valor 5 faz parte da lista e está na {p + 1}º posição!')
        break
else:
    print(' - O valor 5 não faz parte da lista!')
