print('====== DESAFIO 030 ======\n')
n = int(input('\033[31m - Me informe algum número: \033[m'))

if n % 2 == 0:
    print('\033[32m - Esse número é \033[4;33mPAR!\033[m')
if n % 2 == 1:
    print('\033[32m - Esse número é \033[4;33mÍMPAR!\033[m')
