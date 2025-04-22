print('\t\t' + ' DESAFIO 063 '.center(45, '=') + '\n')
print('--' * 20 + '\n\t\tSEQUÊNCIA DE FIBONACCI\n' + '--' * 20)
qtd = int(input(' * Quantos termos deseja imprimir? '))
termo = [0, 0, 1]

for c in range(0, qtd):
    print(termo[0], end=' -> ')
    termo[0] = termo[1] + termo[2]
    termo[2] = termo[1]
    termo[1] = termo[0]

print('FIM')
