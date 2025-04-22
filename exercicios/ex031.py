print('====== DESAFIO 031 ======\n')
km = float(input(' - Olá! A viagem será de quantos KM? '))

if km <= 200:
    valor = km * 0.5
else:
    valor = km * 0.45
# valor = km * 0.5 if km <= 200 else valor = km * 0;45

valorReal = str('%.2f' % valor).replace('.', ',')
print(f' * A sua viagem de \033[33m{km:.1f} KM\033[m ficará no valor de', end=' ')
print(f'\033[4;32mR$ {valorReal}\033[m!')
