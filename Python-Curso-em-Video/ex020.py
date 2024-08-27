from random import sample
print('====== DESAFIO 020 ======\n')
nome1 = input(' 1º aluno: ')
nome2 = input(' 2º aluno: ')
nome3 = input(' 3º aluno: ')
nome4 = input(' 4º aluno: ')
lista = [nome1, nome2, nome3, nome4]
print('\n A ordem de alunos será %s!' % sample(lista, k = 4))
