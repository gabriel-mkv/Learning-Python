from random import choice
print('====== DESAFIO 016 ======\n')
nome1 = input(' - Informe o nome do 1º aluno: ')
nome2 = input(' - Informe o nome do 2º aluno: ')
nome3 = input(' - Informe o nome do 3º aluno: ')
nome4 = input(' - Informe o nome do 4º aluno: ')
lista = [nome1, nome2, nome3, nome4]
print('\n O aluno sorteado foi %s!' % choice(lista))
# print(
#    '\n * O aluno sorteado foi %s!'
#    % choice([nome1, nome2, nome3, nome4]))
