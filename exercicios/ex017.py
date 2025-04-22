from math import hypot
print('====== DESAFIO 017 ======')
catoposto = float(input('\n - Informe o valor do cateto oposto: '))
catadjacente = float(input(' - Informe o valor do cateto adjacente: '))
print('\n * O valor da hipotenusa é %.2f!' % hypot(catoposto, catadjacente))
print('\n' + '=' * 50)
hipotenusa = ((catoposto ** 2) + (catadjacente ** 2)) ** (1/2)
print('\n * O valor da hipotenusa é %.2f!' % hipotenusa)
