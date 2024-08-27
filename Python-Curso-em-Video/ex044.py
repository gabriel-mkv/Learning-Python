opc = 0
valorFinal = 0

print(f'\t\t{' DESAFIO 043 ':=^25}\n')
print(f'{' LOJAS TEHKU ':=^40}\n')
valor = float(input(' - Informe o valor total da compra: R$ '))
print('''\n « FORMAS DE PAGAMENTO »
[ 1 ] À VISTA / CHEQUE
[ 2 ] À VISTA NO CARTÃO    
[ 3 ] 2x NO CARTÃO    
[ 4 ] 3x OU MAIS NO CARTÃO\n''')

while (opc < 1) or (opc > 4):
    opc = int(input(' - Informe a opção de pagamento: '))

if opc == 1:
    valorFinal = valor - (valor * 0.1)
elif opc == 2:
    valorFinal = valor - (valor * 0.05)
elif opc == 3:
    print(f'\n * Sua compra será parcelada 2x de R$ {valor / 2:.2f}')
    print(f' * Sua compra vai custar R$ {valor:.2f}')
    exit()
elif opc == 4:
    valorFinal = valor * 1.2
    nparcelas = int(input(' - Informe o número de parcelas: '))
    valorparcelas = valorFinal / nparcelas
    print(f'\n * Sua compra será parcelada em {nparcelas}x de R$ {valorparcelas:.2f} COM JUROS')
    print(f' * Sua compra vai custar R$ {valorFinal:.2f}')
    exit()

print(f'\n * Sua compra será de R$ {valor:.2f} vai custar R$ {valorFinal:.2f} COM DESCONTO')
