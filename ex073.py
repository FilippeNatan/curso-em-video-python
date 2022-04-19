tuplaBrasileirao = ('Corinthians', 'Atlético-MG', 'Bragantino', 'Flamengo', 'Santos',
                    'Fluminense', 'São Paulo', 'Coritiba', 'América-MG', 'Botafogo',
                    'Cuiabá', 'Ceará', 'Internacional', 'Avaí', 'Palmeiras', 'Juventude',
                    'Goiás', 'Atlético-GO', 'Fortaleza', 'Athletico-PR')
print('='*100)
print('{:^100}'.format('CAMPEONATO BRASILEIRO 19/04/22'))
print('='*100)
print(f'Os cinco primeiros colocados são: {tuplaBrasileirao[0:5]}')
print('='*100)
print(f'Os últimos 4 colocados são: {tuplaBrasileirao[-4:]}')
print('='*100)
print(f'Times por ordem alfabética: {sorted(tuplaBrasileirao)}')
print('='*100)
print(f'O Palmeiras está na {tuplaBrasileirao.index("Palmeiras")+1}ª posição.')
print('='*100)
