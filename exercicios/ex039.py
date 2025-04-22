from datetime import date
from time import sleep
print('\t\t====== DESAFIO 039 ======\n')
print('\t\033[31m ALISTAMENTO MILITAR, O MEDO DE TODO JOVEM!\033[m\n')
nascimento = int(input(' - Informe qual o ano de seu nascimento: '))
idade = (date.today().year - nascimento)
print('\n   Analisando...\n')
sleep(3)

print(f' * Você possui {idade} anos!')

if idade < 18:
    print(f'\033[33m * SEU ALISTAMENTO SERÁ DAQUI A {18 - idade} ANO(S)', end=' ')
    print(f'(EM {date.today().year + (18 - idade)})!\033[m')
elif idade == 18:
    print(f'\033[31m * SEU ALISTAMENTO SERÁ NESSE ANO ({date.today().year})!\033[m')
elif (idade > 18) and (idade < 100):
    print(f'\033[35m * SEU PRAZO PARA SE ALISTAR JÁ PASSOU EM {idade - 18} ANO(S)', end=' ')
    print(f'(FOI EM {date.today().year - (idade - 18)})!\033[m')
else:
    print('\n   ...\n')
    sleep(2)
    print(f'\033[36m * TA VELHO JÁ HEIN PARCEIRO? KKKK\033[m')
