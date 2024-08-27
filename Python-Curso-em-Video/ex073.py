print(' DESAFIO 073 '.center(45, '='))

times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'São Paulo', 'Bahia', 'Cruzeiro',
         'Athletico-PR', 'Bragantino', 'Atlético-MG', 'Vasco', 'Juventude', 'Internacional',
         'Corinthians', 'Criciúma', 'Cuiabá', 'EC Vitória', 'Grêmio', 'Fluminense', 'Atlético-GO')

print('\n' + ' BRASILEIRÃO 2024 '.center(30, '-') + '\n')
for i, t in enumerate(times):
    print(f'\t  {i + 1:2d}º | {t}')

print('\n > 5 PRIMEIROS TIMES: \n')
for p in times[0:5]:
    print(f'{p}', end=' | ')

print('\n\n > 4 ÚLTIMOS TIMES: \n')
for u in times[-4:]:
    print(f'{u}', end=' | ')

print('\n\n > ORDEM ALFABÉTICA: \n')
for a in sorted(times):
    print(f'| {a} ')

print(f'\n > O Vasco está na {times.index('Vasco')}º posição!')
