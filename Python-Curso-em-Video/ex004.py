valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(valor)}')
print(f'É um número? {valor.isnumeric()}')
print(f'É alfanúmerico? {valor.isalnum()}')
print(f'É alfabético? {valor.isalpha()}')
print(f'Está em minúsculas? {valor.islower()}')
print(f'Está em maiúsculas? {valor.isupper()}')
print(f'Só tem espaços? {valor.isspace()}')
