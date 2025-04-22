print(' DESAFIO 082 '.center(45, '='))
lista = []
par = []
impar = []

while True:
    lista.append(int(input('\n > Informe um número: ')))
    opc = input(' - Deseja continuar? [S/N] ').upper()
    if opc == 'N':
        break

for i in lista:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print('-*' * 25)
print(f' - Lista original: {lista}')
print(f' - Lista com pares: {par}')
print(f' - Lista com ímpares: {impar}')