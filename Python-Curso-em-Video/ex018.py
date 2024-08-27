from math import radians, cos, tan, sin
print('====== DESAFIO 018 ======')
angulo = float(input('\n - Informe o ângulo -> '))
radiano = radians(angulo)
print(f'\n * O ângulo de {angulo} tem o SENO de %.2f' % sin(radiano))
print(f' * O ângulo de {angulo} tem o COSSENO de %.2f' % cos(radiano))
print(f' * O ângulo de {angulo} tem a TANGENTE de %.2f' % tan(radiano))
