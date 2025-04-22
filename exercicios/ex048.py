print('\t\t' + ' DESAFIO 048 '.center(45, '=') + '\n')
s = [0, 0]

for c in range(3, 500, 6):
    s[1] += 1
    s[0] += c

print(f' * Entre 1 e 500 existem {s[1]} número ímpares e múltiplos de 3!')
print(f' * A soma entre esses números é {s[0]}!')
