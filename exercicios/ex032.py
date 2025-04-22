from datetime import date
print('====== DESAFIO 032 ======\n')
ano = int(input(' - Informe algum ano (0 para o ano atual) -> '))
unidade = ano // 1 % 10
dezena = ano // 10 % 10

if ano == 0:
    ano = date.today().year

# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

if (unidade != 0) and (dezena != 0):
    if ano % 4 == 0:
        print(f' * O ano de \033[35m{ano}\033[m é \033[4;33mBISSEXTO\033[m!')
    else:
        print(f' * O ano de \033[35m{ano}\033[m NÃO é \033[4;33mBISSEXTO\033[m!')
else:
    if ano % 400 == 0:
        print(f' * O ano de \033[35m{ano}\033[m é \033[4;33mBISSEXTO\033[m!')
    else:
        print(f' * O ano de \033[35m{ano}\033[m NÃO é \033[4;33mBISSEXTO\033[m!')
