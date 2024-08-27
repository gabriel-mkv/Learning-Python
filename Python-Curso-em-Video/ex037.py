print('\t\t====== DESAFIO 037 ======\n')
n = int(input(' - Informe um número inteiro para ser convertido: '))
print('''
    1 - BINÁRIO
    2 - OCTAL
    3 - HEXADECIMAL\n''')
opc = int(input(' - Digite qual opção deseja: '))

if opc == 1:
    print(f' * O número {n} em binário é {n:b}')
elif opc == 2:
    print(f' * O número {n} em octal é {n:o}')
elif opc == 3:
    print(f' * O número {n} em hexadecimal é {n:x}')
else:
    print(' * DIGITE UMA OPÇÃO VÁLIDA!')
