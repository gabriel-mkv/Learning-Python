from time import sleep
print('\t\t====== DESAFIO 042 ======\n')
lado1 = float(input(' - 1º segmento: '))
lado2 = float(input(' - 2º segmento: '))
lado3 = float(input(' - 3º segmento: '))
print('\033[35m=-' * 20)
print('  ANALISANDO TRIÂNGULO...')
print('=-' * 20 + '\033[m')
sleep(2)

if ((lado1 + lado2) > lado3) and ((lado1 + lado3) > lado2) and ((lado2 + lado3) > lado1):
    print(' * Essas medidas formam um triângulo', end=' ')
    if lado1 != lado2 != lado3 != lado1:
        print('ESCALENO!')
    elif lado1 == lado2 == lado3:
        print('EQUILÁTERO!')
    else:
        print('ISÓSCELES!')
else:
    print(' * Essas medidas NÃO PODEM FORMAR um triângulo!')
